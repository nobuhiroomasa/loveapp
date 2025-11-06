"""Command line interface for the Date & Outing AI."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from typing import Any

from .data import BUDGET_LEVELS
from .recommender import DateOutingAI, RecommendationRequest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="date-ai",
        description="デート＆おでかけAI: 気分に合わせたプランをおすすめします",
    )
    parser.add_argument("city", help="出発エリア（例: 東京, 京都）")
    parser.add_argument(
        "--budget",
        choices=list(BUDGET_LEVELS),
        help="想定する予算帯 (¥〜¥プレミアム)",
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
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

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
            print(f"   ムード: {exp.mood} / アクティビティ: {exp.activity_type}")
            print(f"   概要: {exp.description}")
            print(
                f"   ベストシーズン: {exp.ideal_season} / おすすめ時間帯: {exp.ideal_time}"
            )
            booking = "要予約" if exp.booking_required else "当日参加OK"
            print(f"   予約: {booking}")
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


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())

