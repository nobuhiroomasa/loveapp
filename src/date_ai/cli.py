"""Command line interface for the Date & Outing AI."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from typing import Any, Dict

from .data import BUDGET_BANDS, BUDGET_LEVELS
from .recommender import DateOutingAI, RecommendationRequest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="date-ai",
        description="デート＆おでかけAI: 気分に合わせたプランをおすすめします",
    )
    parser.add_argument("city", nargs="?", help="出発エリア（例: 東京, 京都）")
    parser.add_argument(
        "--budget",
        choices=list(BUDGET_LEVELS),
        help="想定する予算帯 (¥ライト〜¥プレミアム)",
    )
    parser.add_argument(
        "--weather",
        choices=["晴れ", "曇り", "雨", "雪"],
        help="想定する天気",
    )
    parser.add_argument(
        "--mood",
        help="どんなムードで過ごしたいか (例: ロマンチック, アクティブ)",
    )
    parser.add_argument(
        "--activity",
        dest="activity_type",
        help="やりたいアクティビティの種類 (例: グルメ, アウトドア)",
    )
    parser.add_argument(
        "--max-hours",
        type=int,
        dest="max_duration_hours",
        help="確保できる最大時間 (時間数)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="表示するおすすめ件数 (デフォルト: 3)",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="出力形式 (text または json)",
    )
    parser.add_argument(
        "--list-budgets",
        action="store_true",
        help="利用可能な予算帯一覧を表示して終了",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if getattr(args, "list_budgets", False):
        _print_budget_table()
        return 0

    if not args.city:
        parser.error("city は必須です。エリアを指定してください。")

    request = RecommendationRequest(
        city=args.city,
        budget=args.budget,
        weather=args.weather,
        mood=args.mood,
        activity_type=args.activity_type,
        max_duration_hours=args.max_duration_hours,
        limit=args.limit,
    )

    ai = DateOutingAI()
    recommendations = ai.recommend(request)

    if args.format == "json":
        payload: list[dict[str, Any]] = []
        for rec in recommendations:
            data = asdict(rec.experience)
            data["score"] = rec.score
            data["rationale"] = list(rec.rationale)
            band = _budget_lookup().get(rec.experience.budget)
            if band:
                data["budget_band"] = {
                    "code": band.code,
                    "label": band.label,
                    "range": band.format_range(),
                    "description": band.description,
                }
            payload.append(data)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if not recommendations:
            print("条件に合うプランが見つかりませんでした。条件を緩めてみてください。")
            return 0

        for idx, rec in enumerate(recommendations, start=1):
            exp = rec.experience
            print(f"[{idx}] {exp.title} ({exp.city})")
            print(f"   スコア: {rec.score:.1f}")
            print(f"   所要時間: 約{exp.duration_hours}時間 / 予算: {exp.budget}")
            band = _budget_lookup().get(exp.budget)
            if band:
                print(
                    f"     ↳ {band.label} (目安: {band.format_range()})"
                )
            print(f"   ムード: {exp.mood} / アクティビティ: {exp.activity_type}")
            print(f"   概要: {exp.description}")
            print(
                f"   ベストシーズン: {exp.ideal_season} / おすすめ時間帯: {exp.ideal_time}"
            )
            booking = "要予約" if exp.booking_required else "当日参加OK"
            print(f"   予約: {booking}")
            if exp.detail:
                detail = exp.detail
                if detail.neighborhood:
                    print(f"   エリア: {detail.neighborhood}")
                if detail.meeting_point:
                    print(f"   集合場所: {detail.meeting_point}")
                if detail.access:
                    print(f"   アクセス: {detail.access}")
                if detail.attire:
                    print(f"   服装メモ: {detail.attire}")
                if detail.website:
                    print(f"   公式情報: {detail.website}")
                if detail.contact:
                    print(f"   問い合わせ: {detail.contact}")
                if detail.languages:
                    print(f"   対応言語: {', '.join(detail.languages)}")
                if detail.suitable_for:
                    print(f"   おすすめシーン: {', '.join(detail.suitable_for)}")
                if detail.cancellation:
                    print(f"   キャンセルポリシー: {detail.cancellation}")
            print("   ハイライト:")
            for highlight in exp.highlights:
                print(f"    - {highlight}")
            if exp.tips:
                print("   プランのコツ:")
                for tip in exp.tips:
                    print(f"    - {tip}")
            print("   推薦ポイント:")
            for reason in rec.rationale:
                print(f"    * {reason}")
            print()

    return 0


_BUDGET_CACHE: Dict[str, "BudgetBand"] | None = None


def _budget_lookup() -> Dict[str, "BudgetBand"]:
    global _BUDGET_CACHE
    if _BUDGET_CACHE is None:
        _BUDGET_CACHE = {band.code: band for band in BUDGET_BANDS}
    return _BUDGET_CACHE


def _print_budget_table() -> None:
    print("利用できる予算帯:")
    print("------------------")
    for band in BUDGET_BANDS:
        print(f"{band.code}: {band.label}")
        print(f"  目安: {band.format_range()}")
        print(f"  概要: {band.description}")
        print()


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())

