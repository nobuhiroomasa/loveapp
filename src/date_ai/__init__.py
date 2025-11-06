"""Date & Outing AI package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .data import BUDGET_LEVELS
from .recommender import DateOutingAI, Recommendation, RecommendationRequest

if TYPE_CHECKING:  # pragma: no cover - import only for typing
    from flask import Flask


def create_app() -> "Flask":
    """Return a configured Flask application instance."""

    from .web import create_app as factory

    return factory()


__all__ = [
    "DateOutingAI",
    "RecommendationRequest",
    "Recommendation",
    "create_app",
    "BUDGET_LEVELS",
]
