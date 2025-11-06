"""Recommendation engine for the Date & Outing AI."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Sequence

from .data import EXPERIENCES, Experience

CITY_ALIASES: Dict[str, str] = {
    "tokyo": "東京",
    "kyoto": "京都",
    "osaka": "大阪",
    "sapporo": "札幌",
    "fukuoka": "福岡",
    "yokohama": "横浜",
    "nagoya": "名古屋",
    "naha": "那覇",
    "kobe": "神戸",
}


@dataclass
class RecommendationRequest:
    """Parameters describing the desired outing."""

    city: str | None = None
    budget: str | None = None
    weather: str | None = None
    mood: str | None = None
    activity_type: str | None = None
    max_duration_hours: int | None = None
    limit: int = 3


@dataclass
class Recommendation:
    """A single recommendation enriched with reasoning."""

    experience: Experience
    score: float
    rationale: Sequence[str] = field(default_factory=tuple)

    @property
    def title(self) -> str:
        return self.experience.title

    @property
    def description(self) -> str:
        return self.experience.description


class DateOutingAI:
    """Simple rule-based recommender for curated date ideas."""

    def __init__(self, experiences: Iterable[Experience] | None = None) -> None:
        self._experiences: List[Experience] = list(experiences or EXPERIENCES)
        if not self._experiences:
            raise ValueError("At least one experience is required")

    def recommend(self, request: RecommendationRequest) -> List[Recommendation]:
        """Return the best matching experiences for the request."""

        scored: List[Recommendation] = []
        normalized_city_value = _canonical_city(request.city)
        city_normalized = _normalize(normalized_city_value)
        for exp in self._experiences:
            if city_normalized and city_normalized not in _normalize(exp.city):
                continue

            score = 0.0
            rationale: List[str] = []

            if city_normalized:
                score += 2.0
                rationale.append(f"リクエストのエリア（{exp.city}）にマッチ")

            if request.budget and request.budget == exp.budget:
                score += 1.0
                rationale.append(f"予算帯 {exp.budget} が一致")

            if request.weather and request.weather == exp.weather:
                score += 1.0
                rationale.append(f"想定天気 {exp.weather} に対応")

            if request.mood and request.mood == exp.mood:
                score += 1.0
                rationale.append(f"ムード {exp.mood} にフィット")

            if request.activity_type and request.activity_type == exp.activity_type:
                score += 0.5
                rationale.append(f"アクティビティ種別 {exp.activity_type} が一致")

            if (
                request.max_duration_hours is not None
                and exp.duration_hours <= request.max_duration_hours
            ):
                score += 0.5
                rationale.append("希望時間内で実現可能")
            elif request.max_duration_hours is not None:
                score -= 0.5
                rationale.append(
                    f"所要時間が{exp.duration_hours}時間で、希望({request.max_duration_hours}時間以内)を少し超えます"
                )

            # Provide a light popularity boost via highlight count.
            score += min(len(exp.highlights) * 0.1, 0.3)

            if score > 0:
                scored.append(
                    Recommendation(
                        experience=exp,
                        score=score,
                        rationale=tuple(rationale) or ("幅広いニーズに応えるおすすめプラン",),
                    )
                )

        scored.sort(key=lambda rec: rec.score, reverse=True)
        limit = max(1, request.limit)
        return scored[:limit]


def _normalize(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip().lower()


def _canonical_city(value: str | None) -> str:
    if value is None:
        return ""

    trimmed = value.strip()
    if not trimmed:
        return ""

    lookup_key = trimmed.lower()
    return CITY_ALIASES.get(lookup_key, trimmed)

