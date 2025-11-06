"""Flask-based web interface for the Date & Outing AI."""

from __future__ import annotations

import importlib.util
from dataclasses import asdict
from typing import Any, Dict, List, Optional

if importlib.util.find_spec("flask") is None:  # pragma: no cover - import guard
    raise RuntimeError(
        "Flask が見つかりません。`pip install -r requirements.txt` を実行して依存関係を"
        "インストールしてください。"
    )

from flask import Flask, render_template, request

from .data import EXPERIENCES
from .recommender import DateOutingAI, Recommendation, RecommendationRequest


def _collect_choices() -> Dict[str, List[str]]:
    cities = sorted({exp.city for exp in EXPERIENCES})
    budgets = sorted({exp.budget for exp in EXPERIENCES})
    weathers = sorted({exp.weather for exp in EXPERIENCES})
    moods = sorted({exp.mood for exp in EXPERIENCES})
    activity_types = sorted({exp.activity_type for exp in EXPERIENCES})
    return {
        "cities": cities,
        "budgets": budgets,
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
    data = asdict(rec.experience)
    data.update(
        {
            "score": rec.score,
            "rationale": list(rec.rationale),
        }
    )
    return data


def main() -> None:
    app = create_app()
    host = "0.0.0.0"
    port = 8000
    print(f"🚀 デート＆おでかけAI Web が http://127.0.0.1:{port} で利用可能です (Ctrl+C で終了)")
    app.run(debug=False, host=host, port=port)


if __name__ == "__main__":  # pragma: no cover - manual launch helper
    main()
