"""Flask-based web interface for the Date & Outing AI."""

from __future__ import annotations

import importlib.util
import argparse
from dataclasses import asdict
from typing import Any, Dict, List, Optional

if importlib.util.find_spec("flask") is None:  # pragma: no cover - import guard
    raise RuntimeError(
        "Flask が見つかりません。`pip install -r requirements.txt` を実行して依存関係を"
        "インストールしてください。"
    )

from flask import Flask, render_template, request

from .data import BUDGET_BANDS, BUDGET_LEVELS, EXPERIENCES, BudgetBand
from .recommender import DateOutingAI, Recommendation, RecommendationRequest


_BUDGET_LOOKUP: Dict[str, BudgetBand] = {band.code: band for band in BUDGET_BANDS}


def _collect_choices() -> Dict[str, Any]:
    cities = sorted({exp.city for exp in EXPERIENCES})
    budget_set = {exp.budget for exp in EXPERIENCES}
    budgets = [level for level in BUDGET_LEVELS if level in budget_set]
    weathers = sorted({exp.weather for exp in EXPERIENCES})
    moods = sorted({exp.mood for exp in EXPERIENCES})
    activity_types = sorted({exp.activity_type for exp in EXPERIENCES})
    return {
        "cities": cities,
        "budgets": budgets,
        "budget_bands": BUDGET_BANDS,
        "weathers": weathers,
        "moods": moods,
        "activity_types": activity_types,
    }


CHOICES = _collect_choices()


def create_app() -> Flask:
    """Application factory for the web experience."""

    app = Flask(__name__)
    engine = DateOutingAI()

    @app.context_processor
    def inject_choices() -> Dict[str, Any]:
        return {
            "choices": CHOICES,
        }

    @app.route("/", methods=["GET", "POST"])
    def index() -> str:
        form_data = _default_form()
        recommendations: List[Recommendation] = []
        message: Optional[str] = None

        if request.method == "POST":
            form_data = _parse_form(request.form)
            if not form_data["city"]:
                message = "エリアを選択してください。"
            else:
                rec_request = RecommendationRequest(
                    city=form_data["city"],
                    budget=form_data.get("budget") or None,
                    weather=form_data.get("weather") or None,
                    mood=form_data.get("mood") or None,
                    activity_type=form_data.get("activity_type") or None,
                    max_duration_hours=form_data.get("max_duration_hours"),
                    limit=form_data.get("limit", 3) or 3,
                )
                recommendations = engine.recommend(rec_request)
                if not recommendations:
                    message = "条件に合うプランが見つかりませんでした。条件を緩めてみてください。"
        else:
            # allow shareable query parameters like /?city=東京&limit=5
            if request.args:
                form_data = _parse_form(request.args)
                if form_data["city"]:
                    rec_request = RecommendationRequest(
                        city=form_data["city"],
                        budget=form_data.get("budget") or None,
                        weather=form_data.get("weather") or None,
                        mood=form_data.get("mood") or None,
                        activity_type=form_data.get("activity_type") or None,
                        max_duration_hours=form_data.get("max_duration_hours"),
                        limit=form_data.get("limit", 3) or 3,
                    )
                    recommendations = engine.recommend(rec_request)
                    if not recommendations:
                        message = "条件に合うプランが見つかりませんでした。条件を緩めてみてください。"

        return render_template(
            "index.html",
            form=form_data,
            recommendations=[_serialize_recommendation(rec) for rec in recommendations],
            message=message,
        )

    @app.route("/healthz")
    def healthcheck() -> str:
        return "ok"

    return app


def _default_form() -> Dict[str, Any]:
    return {
        "city": "",
        "budget": "",
        "weather": "",
        "mood": "",
        "activity_type": "",
        "max_duration_hours": "",
        "limit": 3,
    }


def _parse_form(mapping: Any) -> Dict[str, Any]:
    form = _default_form()
    form.update({key: (mapping.get(key) or "").strip() for key in form.keys() if key != "limit"})

    limit_raw = mapping.get("limit") if hasattr(mapping, "get") else None
    try:
        limit_value = int(limit_raw) if limit_raw else 3
        form["limit"] = max(1, min(limit_value, 10))
    except (TypeError, ValueError):
        form["limit"] = 3

    max_hours_raw = mapping.get("max_duration_hours") if hasattr(mapping, "get") else None
    try:
        form["max_duration_hours"] = int(max_hours_raw) if max_hours_raw else None
    except (TypeError, ValueError):
        form["max_duration_hours"] = None

    return form


def _serialize_recommendation(rec: Recommendation) -> Dict[str, Any]:
    exp_dict = asdict(rec.experience)
    detail = exp_dict.get("detail")
    if isinstance(detail, dict):
        exp_dict["detail"] = {
            key: value
            for key, value in detail.items()
            if (value or value == 0) and (not isinstance(value, list) or value)
        }

    band = _BUDGET_LOOKUP.get(rec.experience.budget)
    if band:
        exp_dict["budget_band"] = {
            "code": band.code,
            "label": band.label,
            "range": band.format_range(),
            "description": band.description,
        }

    exp_dict.update(
        {
            "score": rec.score,
            "rationale": list(rec.rationale),
        }
    )
    return exp_dict


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Date & Outing AI Web サーバー")
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="待ち受けるホスト名。ローカルのみで使う場合は 127.0.0.1 を指定できます。",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="待ち受けポート番号 (既定: 8000)。使用中の場合は別ポートを指定してください。",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    app = create_app()
    display_host = "127.0.0.1" if args.host in {"0.0.0.0", "::"} else args.host
    print(
        f"🚀 デート＆おでかけAI Web が http://{display_host}:{args.port} で利用可能です "
        "(Ctrl+C で終了)"
    )
    app.run(debug=False, host=args.host, port=args.port, use_reloader=False)


if __name__ == "__main__":  # pragma: no cover - manual launch helper
    main()
