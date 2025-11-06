"""Sample experiences database for the Date & Outing AI."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Experience:
    """Represents a curated date or outing idea."""

    city: str
    title: str
    description: str
    activity_type: str
    budget: str
    weather: str
    mood: str
    duration_hours: int
    highlights: List[str]


EXPERIENCES: Iterable[Experience] = (
    Experience(
        city="東京",
        title="隅田川沿いナイトピクニック",
        description=(
            "夕暮れに合わせて隅田川沿いを散策し、夜景を眺めながら軽食を楽しむ"
            "ロマンチックなピクニックプラン。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["スカイツリーの夜景", "川沿いの静かな時間", "気軽に楽しめる軽食"],
    ),
    Experience(
        city="東京",
        title="表参道アートギャラリー巡り",
        description=(
            "表参道周辺のギャラリーを散策し、お気に入りの作品を探しながら"
            "おしゃれなカフェでひと休みするカルチャーデート。"
        ),
        activity_type="インドア",
        budget="¥¥",
        weather="雨",
        mood="知的",
        duration_hours=4,
        highlights=["最新アートとの出会い", "ギャラリーカフェ", "ショッピングも楽しめる"],
    ),
    Experience(
        city="京都",
        title="嵐山サイクリングと竹林散歩",
        description=(
            "レンタサイクルで嵐山を巡り、渡月橋や竹林の小径を散歩する"
            "アクティブな自然満喫プラン。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=5,
        highlights=["渡月橋の絶景", "竹林の静けさ", "自転車での爽快感"],
    ),
    Experience(
        city="大阪",
        title="中之島ジャズバー＆リバークルーズ",
        description=(
            "夕方のリバークルーズで川辺の景色を楽しんだあと、"
            "ジャズバーで大人な時間を過ごすナイトデート。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="曇り",
        mood="ラグジュアリー",
        duration_hours=4,
        highlights=["リバークルーズ", "生演奏のジャズ", "夜景スポット"],
    ),
    Experience(
        city="札幌",
        title="大通公園ホットチョコさんぽ",
        description=(
            "冬の大通公園をイルミネーションとともに散策し、"
            "ホットチョコレートで温まるほっこりデート。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="雪",
        mood="リラックス",
        duration_hours=2,
        highlights=["イルミネーション", "冬の散歩", "ホットドリンク"],
    ),
    Experience(
        city="福岡",
        title="屋台グルメはしごツアー",
        description=(
            "中洲エリアの屋台を食べ歩き、地元グルメをとことん味わう"
            "カジュアルでにぎやかな夜のおでかけ。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="晴れ",
        mood="カジュアル",
        duration_hours=3,
        highlights=["豚骨ラーメン", "焼きラーメン", "地元の人との交流"],
    ),
    Experience(
        city="横浜",
        title="みなとみらい夜景クルーズ",
        description=(
            "みなとみらいの夜景を船上から楽しみ、デッキで写真撮影を"
            "満喫する特別なデート。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ドラマチック",
        duration_hours=2,
        highlights=["ベイブリッジの夜景", "クルーズディナー", "写真映えスポット"],
    ),
    Experience(
        city="名古屋",
        title="徳川園ライトアップ散策",
        description=(
            "ライトアップされた日本庭園をゆっくり散策し、歴史と自然を"
            "感じるしっとりとした夜のおでかけ。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="落ち着き",
        duration_hours=2,
        highlights=["ライトアップ庭園", "写真撮影", "和カフェでの休憩"],
    ),
    Experience(
        city="那覇",
        title="首里城周辺の夕景散策",
        description=(
            "夕暮れ時の首里城公園を散策し、沖縄の歴史と文化に触れる"
            "癒やしのお散歩デート。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=2,
        highlights=["首里城の夕景", "沖縄伝統舞踊の鑑賞", "地元スイーツ"],
    ),
    Experience(
        city="神戸",
        title="北野異人館カフェ巡り",
        description=(
            "北野異人館街でレトロな建物を巡りながら、趣のあるカフェで"
            "まったり過ごすおでかけプラン。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="曇り",
        mood="リラックス",
        duration_hours=3,
        highlights=["異人館の建築", "レトロカフェ", "雑貨ショップ"],
    ),
)

