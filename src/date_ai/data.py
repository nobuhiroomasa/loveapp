"""Curated experiences database for the Date & Outing AI."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import List, Mapping, Tuple


@dataclass(frozen=True)
class BudgetBand:
    """Describes a selectable budget tier."""

    code: str
    label: str
    per_person_min: int | None
    per_person_max: int | None
    description: str

    def format_range(self) -> str:
        """Return a human friendly range string."""

        if self.per_person_min is None and self.per_person_max is None:
            return "指定なし"
        if self.per_person_min is None:
            return f"〜¥{self.per_person_max:,}"
        if self.per_person_max is None:
            return f"¥{self.per_person_min:,}〜"
        return f"¥{self.per_person_min:,}〜¥{self.per_person_max:,}"


BUDGET_BANDS: Tuple[BudgetBand, ...] = (
    BudgetBand(
        code="¥ライト",
        label="ライト (カフェ＆散歩中心)",
        per_person_min=None,
        per_person_max=4000,
        description="ドリンクやスイーツ、散策を気軽に楽しむプラン向け",
    ),
    BudgetBand(
        code="¥",
        label="スタンダード (カジュアル外食)",
        per_person_min=4000,
        per_person_max=8000,
        description="休日の外食やアクティビティを無理なく組み合わせたいとき",
    ),
    BudgetBand(
        code="¥¥",
        label="リッチ (人気店＆体験)",
        per_person_min=8000,
        per_person_max=15000,
        description="話題のレストランや体験プログラムを含む充実プラン",
    ),
    BudgetBand(
        code="¥¥プラス",
        label="ハイグレード (ちょっと贅沢)",
        per_person_min=15000,
        per_person_max=22000,
        description="記念日ディナーや少人数ツアーなどワンランク上を狙う",
    ),
    BudgetBand(
        code="¥¥¥",
        label="アニバーサリー (特別な日)",
        per_person_min=22000,
        per_person_max=35000,
        description="アニバーサリーやプロポーズで活用したい本格プラン",
    ),
    BudgetBand(
        code="¥¥¥¥",
        label="ラグジュアリー (高級体験)",
        per_person_min=35000,
        per_person_max=55000,
        description="高級ホテルスパや貸切体験などプレミアムな時間",
    ),
    BudgetBand(
        code="¥プレミアム",
        label="プレミアム (究極のご褒美)",
        per_person_min=55000,
        per_person_max=None,
        description="一生の思い出に残るラグジュアリーな過ごし方",
    ),
)

BUDGET_LEVELS: Tuple[str, ...] = tuple(band.code for band in BUDGET_BANDS)


@dataclass(frozen=True)
class ExperienceDetail:
    """Additional optional metadata for an experience."""

    neighborhood: str = ""
    meeting_point: str = ""
    access: str = ""
    website: str = ""
    contact: str = ""
    attire: str = ""
    cancellation: str = ""
    languages: List[str] = field(default_factory=list)
    suitable_for: List[str] = field(default_factory=list)


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
    ideal_season: str = "オールシーズン"
    ideal_time: str = "終日"
    tips: List[str] = field(default_factory=list)
    booking_required: bool = False
    detail: ExperienceDetail | None = None


RAW_EXPERIENCES: Tuple[Experience, ...] = (
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
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["レジャーシートと軽食は浅草で調達", "夜風が冷えるので薄手のブランケットを持参"],
    ),
    Experience(
        city="東京",
        title="吉祥寺モーニング散歩と井の頭ボート",
        description=(
            "開店直後の吉祥寺カフェでモーニングを楽しんだあと、井の頭恩賜公園で"
            "朝のボート遊びと緑あふれる散策を味わうヘルシースタート。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["吉祥寺のベーカリー", "井の頭池のボート", "朝の静かな動物園"],
        ideal_season="春〜初夏",
        ideal_time="午前",
        tips=["ボートは9時の営業開始直後が空いていて狙い目", "動物園は入園再開時間を事前チェック"],
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
        ideal_season="オールシーズン",
        ideal_time="午後〜夕方",
        tips=["混雑を避けるなら平日がおすすめ", "最後は青山通り沿いの人気カフェで一息"],
    ),
    Experience(
        city="東京",
        title="銀座ミシュランディナーと夜景バー",
        description=(
            "銀座のミシュラン掲載店で旬のコースを味わい、"
            "食後は丸の内の高層バーで夜景とシグネチャーカクテルを楽しむラグジュアリープラン。"
        ),
        activity_type="グルメ",
        budget="¥プレミアム",
        weather="晴れ",
        mood="ラグジュアリー",
        duration_hours=5,
        highlights=["ミシュラン星付きの味", "夜景の見える特等席", "ソムリエ厳選のペアリング"],
        ideal_season="オールシーズン",
        ideal_time="夜",
        tips=["2週間前までの予約が安心", "ドレスコードに注意"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="神楽坂フレンチと路地裏バー梯子",
        description=(
            "神楽坂の石畳エリアで季節のコース料理を味わい、食後は路地裏の隠れ家バーで"
            "クラフトカクテルを楽しむ大人のグルメナイト。"
        ),
        activity_type="グルメ",
        budget="¥¥プラス",
        weather="晴れ",
        mood="ラグジュアリー",
        duration_hours=4,
        highlights=["ミシュランビブグルマンのフレンチ", "ソムリエおすすめワイン", "会員制バーの雰囲気"],
        ideal_season="オールシーズン",
        ideal_time="夜",
        tips=["コースは2日前までに予約", "バーはカジュアルスマートな装いが安心"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="谷中レトロ散歩と抹茶ワークショップ",
        description=(
            "谷中銀座の昔ながらの商店街を散策し、町家茶室で本格的な抹茶点てを体験する癒やしの半日。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=4,
        highlights=["猫のいる路地散策", "職人の抹茶講座", "手作り和菓子付き"],
        ideal_season="春・秋",
        ideal_time="午前〜午後",
        tips=["抹茶ワークショップは前日までに要予約", "歩きやすい靴を選ぶ"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="お台場サンセットクルーズと夜景ディナー",
        description=(
            "お台場海浜公園を散策したあと、東京湾を周遊するサンセットクルーズで"
            "ベイエリアの夜景とフレンチコースを楽しむシーサイドプラン。"
        ),
        activity_type="クルーズ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=5,
        highlights=["レインボーブリッジの夜景", "船上シャンパンサービス", "デッキからの写真撮影"],
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["乗船30分前までに受付を済ませる", "風が強い日は薄手の羽織を持参"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="下北沢レコードハンティングとライブハウスナイト",
        description=(
            "下北沢のレコードショップを巡ってお気に入りの音源を探し、"
            "夜は老舗ライブハウスでインディーズバンドのステージを楽しむ音楽漬けの一日。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=6,
        highlights=["掘り出し物のアナログ盤", "ライブ前のクラフトビール", "アーティストとの交流"],
        ideal_season="オールシーズン",
        ideal_time="午後〜夜",
        tips=["ライブチケットは事前に予約", "耳栓を用意すると安心"],
        booking_required=True,
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
        ideal_season="春・秋",
        ideal_time="午前〜夕方",
        tips=["朝早く出発すると人混みを避けられる", "竹林では自転車を押して歩行"],
    ),
    Experience(
        city="京都",
        title="出町柳モーニングと鴨川ベンチデート",
        description=(
            "鴨川デルタ近くの人気ベーカリーでテイクアウトをして、川沿いのベンチで"
            "朝の空気を楽しみながらゆったり朝食をとる京都らしいスタート。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リラックス",
        duration_hours=2,
        highlights=["鴨川デルタの景観", "出町ふたばの豆餅", "朝の京町家街散歩"],
        ideal_season="春〜秋",
        ideal_time="早朝〜午前",
        tips=["デルタの石段は滑りやすいので歩きやすい靴で", "土日は混雑前の8時台が安心"],
    ),
    Experience(
        city="京都",
        title="京町家プライベート茶会",
        description=(
            "築100年の京町家を貸し切り、茶道家による茶会と懐石を体験する伝統文化プラン。"
        ),
        activity_type="カルチャー",
        budget="¥¥¥",
        weather="雨",
        mood="伝統",
        duration_hours=3,
        highlights=["亭主の点前", "季節の主菓子", "床の間のしつらえ"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["着物レンタルを合わせると雰囲気が高まる", "到着は開始10分前を目安に"],
        booking_required=True,
    ),
    Experience(
        city="京都",
        title="先斗町おまかせ割烹と祇園ナイトウォーク",
        description=(
            "先斗町の川床を望む割烹で旬のおまかせコースをいただき、食後は祇園白川を"
            "そぞろ歩きながら町家バーで京カクテルを楽しむしっとりプラン。"
        ),
        activity_type="グルメ",
        budget="¥¥プラス",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["鴨川を眺める川床席", "料理長のおまかせコース", "祇園町家バー"],
        ideal_season="初夏〜初秋",
        ideal_time="夜",
        tips=["川床は5〜9月限定。雨天時は店内席へ", "祇園は石畳なのでヒールは低めがおすすめ"],
        booking_required=True,
    ),
    Experience(
        city="京都",
        title="鴨川サンセットピクニック",
        description=(
            "三条大橋近くでテイクアウトを用意し、鴨川沿いで夕暮れを眺めながらリラックスする定番デート。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=2,
        highlights=["鴨川の夕景", "川辺の涼しい風", "京おばんざいテイクアウト"],
        ideal_season="春〜初秋",
        ideal_time="夕方",
        tips=["レジャーシートの貸し出しサービスを利用", "雨天時は近隣カフェへプランB"],
    ),
    Experience(
        city="京都",
        title="鞍馬ハイキングと貴船川床ディナー",
        description=(
            "叡山電鉄で鞍馬へ向かい自然豊かな参道をハイキングしたあと、"
            "貴船の川床で季節会席を味わう涼やかな山旅プラン。"
        ),
        activity_type="アウトドア",
        budget="¥¥プラス",
        weather="曇り",
        mood="アドベンチャー",
        duration_hours=7,
        highlights=["鞍馬寺から木の根道", "貴船神社での参拝", "川床のせせらぎディナー"],
        ideal_season="初夏〜初秋",
        ideal_time="午前〜夜",
        tips=["ハイキングシューズ必須", "川床は雨天で中止になる場合があるため代替店を確認"],
        booking_required=True,
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
        ideal_season="春〜秋",
        ideal_time="夜",
        tips=["雨天時はクルーズ便の運航状況を確認", "バーはミュージックチャージあり"],
        booking_required=True,
    ),
    Experience(
        city="大阪",
        title="堀江クラフトグルメツアー",
        description=(
            "堀江エリアのクラフトビールタップルームやロースタリーを巡り、"
            "路地裏のスイーツも楽しむ食いだおれ散策。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="曇り",
        mood="カジュアル",
        duration_hours=4,
        highlights=["限定クラフトビール", "自家焙煎コーヒー", "フォトジェニックなスイーツ"],
        ideal_season="オールシーズン",
        ideal_time="午後〜夜",
        tips=["テイスティングセットを共有すると多品種味わえる", "歩きやすい靴がおすすめ"],
    ),
    Experience(
        city="大阪",
        title="万博記念公園ナイトイルミネーション",
        description=(
            "太陽の塔を彩る季節限定イルミネーションとライトアップされた日本庭園を巡る幻想的な夜散歩。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="ドラマチック",
        duration_hours=3,
        highlights=["太陽の塔プロジェクションマッピング", "夜の日本庭園", "屋台フード"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["入場チケットはオンライン購入がスムーズ", "防寒対策をしっかり"],
        booking_required=True,
    ),
    Experience(
        city="大阪",
        title="中崎町古着めぐりと路地裏カフェ",
        description=(
            "レトロな町並みが残る中崎町で古着屋と雑貨店を巡り、路地裏カフェで"
            "自家焙煎コーヒーを楽しむ気軽な街歩きプラン。"
        ),
        activity_type="カルチャー",
        budget="¥ライト",
        weather="晴れ",
        mood="カジュアル",
        duration_hours=3,
        highlights=["ヴィンテージ古着ハント", "アートな路地", "自家焙煎コーヒー"],
        ideal_season="春・秋",
        ideal_time="午後",
        tips=["お気に入りのお店は現金のみの場合あり", "カフェは席数が少ないのでピーク時間を外す"],
    ),
    Experience(
        city="大阪",
        title="梅田スカイビル空中庭園と夜景ディナー",
        description=(
            "梅田スカイビルで夕景から夜景への移ろいを楽しみ、"
            "最上階のレストランでコースディナーを味わうシティビュー体験。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ラグジュアリー",
        duration_hours=4,
        highlights=["空中庭園展望台", "都会の夜景写真スポット", "シャンパン付きコースディナー"],
        ideal_season="オールシーズン",
        ideal_time="夕方〜夜",
        tips=["展望台はサンセット前の入場が狙い目", "ディナーは窓側席を事前指名"],
        booking_required=True,
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
        ideal_season="冬",
        ideal_time="夕方〜夜",
        tips=["耐寒グローブを持参", "路面が滑りやすいので靴底に注意"],
    ),
    Experience(
        city="札幌",
        title="藻岩山ロープウェイ星空ディナー",
        description=(
            "藻岩山山頂展望台で星空と夜景を眺めつつ、コースディナーを味わうロマンチックな夜。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["日本新三大夜景", "山頂レストランのフルコース", "星空観賞"],
        ideal_season="冬〜春",
        ideal_time="夜",
        tips=["ロープウェイの運休情報を確認", "山頂は冷えるので厚手のコートを"],
        booking_required=True,
    ),
    Experience(
        city="札幌",
        title="円山動物園アフターダーク探検",
        description=(
            "閉園後の円山動物園を飼育員のガイドで巡り、夜行性動物の行動観察を楽しむエデュテインメント。"
        ),
        activity_type="エデュテインメント",
        budget="¥¥",
        weather="曇り",
        mood="好奇心",
        duration_hours=3,
        highlights=["夜行性動物の生態", "バックヤード見学", "限定グッズ"],
        ideal_season="夏",
        ideal_time="夜",
        tips=["集合時間に余裕をもって到着", "歩きやすいスニーカーを着用"],
        booking_required=True,
    ),
    Experience(
        city="札幌",
        title="大通公園イルミネーションと夜景ディナー",
        description=(
            "冬の大通公園イルミネーションを散歩し、JRタワー展望室で札幌の夜景を眺めながら"
            "北海道産食材のフレンチディナーを味わうロマンティックコース。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="雪",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["光のトンネル", "展望室からの夜景", "道産食材のコース"],
        ideal_season="冬",
        ideal_time="夕方〜夜",
        tips=["防寒対策を万全に", "イルミネーション終了時間に注意"],
        booking_required=True,
    ),
    Experience(
        city="札幌",
        title="モエレ沼公園ピクニックとガラスのピラミッド",
        description=(
            "イサム・ノグチ設計のモエレ沼公園で芝生ピクニックを楽しみ、"
            "ガラスのピラミッド内のカフェでアートと景色を満喫するデザイン体験。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リラックス",
        duration_hours=5,
        highlights=["プレイマウンテン登頂", "サイクルコース散策", "ピラミッドカフェ"],
        ideal_season="春〜秋",
        ideal_time="午前〜夕方",
        tips=["レンタサイクルは数に限りがあるため午前中に確保", "芝生に座るためのレジャーシートを持参"],
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
        ideal_season="春〜秋",
        ideal_time="夜",
        tips=["人気店は行列必至なので2〜3軒目も候補を", "現金の小銭を用意"],
    ),
    Experience(
        city="福岡",
        title="大濠公園モーニングジョグと湖畔カフェ",
        description=(
            "大濠公園をゆったりジョギングしたあと、湖畔テラスのカフェで"
            "季節のスムージーと軽食を味わう朝活プラン。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="ヘルシー",
        duration_hours=2,
        highlights=["湖畔の朝日", "ジョギングコース", "テラス席カフェ"],
        ideal_season="春〜秋",
        ideal_time="早朝",
        tips=["6時台はランナーが少なく走りやすい", "カフェは現金と電子決済の両方対応"],
    ),
    Experience(
        city="福岡",
        title="糸島サンセットグランピング",
        description=(
            "糸島の海沿いグランピング施設でバーベキューと焚き火を楽しみ、星空を眺めるアウトドア滞在。"
        ),
        activity_type="アウトドア",
        budget="¥¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=8,
        highlights=["海に沈む夕日", "地元食材のBBQ", "個別テントサウナ"],
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["1か月前の予約で人気日程も確保しやすい", "海風が冷えるのでパーカーを"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="柳川川下りと鰻せいろ蒸しランチ",
        description=(
            "柳川の掘割をどんこ舟で巡り、水上から城下町の景観を楽しんだあと、"
            "名物の鰻のせいろ蒸しランチを味わう風情たっぷりの日帰り小旅行。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="伝統",
        duration_hours=5,
        highlights=["船頭さんの唄", "白壁の町並み", "柳川名物の鰻"],
        ideal_season="春〜秋",
        ideal_time="午前〜午後",
        tips=["船の予約は2日前までに", "夏場は日除けの帽子を持参"],
        booking_required=True,
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
        ideal_season="春〜秋",
        ideal_time="夜",
        tips=["乗船30分前には桟橋に集合", "デッキに出る場合は上着を"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="赤レンガクラフトビール＆ジャズ",
        description=(
            "赤レンガ倉庫で開催されるクラフトビールフェスを堪能し、夜はジャズライブハウスで余韻を味わう大人の休日。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="曇り",
        mood="カジュアル",
        duration_hours=5,
        highlights=["限定ブルワリー", "フードトラック", "ライブ演奏"],
        ideal_season="春・秋",
        ideal_time="午後〜夜",
        tips=["ビールフェスはチケット制。早割を利用", "会場は混雑するので待ち合わせは早めに"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="三溪園早朝フォト散策",
        description=(
            "開園直後の三溪園を静かに散策し、茶屋で朝粥セットを味わう癒やしのモーニング。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["朝霧に包まれた庭園", "古建築のフォトスポット", "茶屋の朝食"],
        ideal_season="春・秋",
        ideal_time="早朝",
        tips=["三脚利用は申請が必要", "開園5分前には正門に到着"],
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
        ideal_season="初夏・秋",
        ideal_time="夜",
        tips=["ライトアップは期間限定。公式サイトで日程確認", "三脚使用は制限あり"],
    ),
    Experience(
        city="名古屋",
        title="名古屋城ナイトプロジェクション",
        description=(
            "名古屋城天守をスクリーンにしたプロジェクションマッピングと和太鼓ライブを楽しむ迫力プログラム。"
        ),
        activity_type="カルチャー",
        budget="¥¥¥",
        weather="晴れ",
        mood="ドラマチック",
        duration_hours=3,
        highlights=["3Dプロジェクション", "和太鼓ライブ", "期間限定フード"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["会場は屋外なので防寒必須", "整理券の配布時間を事前に確認"],
        booking_required=True,
    ),
    Experience(
        city="仙台",
        title="定禅寺通りケヤキ並木ライトアップ散歩",
        description=(
            "定禅寺通りのイルミネーションを歩き、終わりにライブハウスでジャズを楽しむ大人の夜。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雪",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["光のページェント", "ケヤキ並木の幻想的な光", "生演奏ジャズ"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["防寒具をしっかり", "ライブハウスはドリンクオーダー制"],
        booking_required=True,
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
        ideal_season="冬〜春",
        ideal_time="夕方",
        tips=["ライトアップ点灯時間を事前に確認", "階段が多いので歩きやすい靴で"],
    ),
    Experience(
        city="那覇",
        title="北谷サンライズSUPと朝食",
        description=(
            "北谷の海でサンライズSUPを体験したあと、海辺カフェでトロピカルブランチを楽しむ爽快な朝時間。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=4,
        highlights=["朝焼けの海", "SUPインストラクターのサポート", "ローカルスムージー"],
        ideal_season="春〜秋",
        ideal_time="早朝",
        tips=["水着の上にラッシュガードを着用", "前夜はアルコール控えめに"],
        booking_required=True,
    ),
    Experience(
        city="那覇",
        title="美ら海水族館と古宇利島サンセットドライブ",
        description=(
            "レンタカーで本部半島へ向かい、美ら海水族館でジンベエザメを鑑賞。"
            "帰路は古宇利大橋からサンセットを楽しむ王道ドライブプラン。"
        ),
        activity_type="ドライブ",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=8,
        highlights=["黒潮の海大水槽", "熱帯魚ショー", "古宇利ブルーの絶景"],
        ideal_season="春〜秋",
        ideal_time="午前〜夕方",
        tips=["高速道路のETC割引を活用", "水族館のショースケジュールを事前確認"],
    ),
    Experience(
        city="那覇",
        title="那覇クラフトビールと島唄ライブバー",
        description=(
            "那覇市内のマイクロブルワリーでテイスティングを楽しんだあと、"
            "国際通り近くのライブバーで三線と島唄のステージを満喫するナイトカルチャー。"
        ),
        activity_type="ナイトライフ",
        budget="¥",
        weather="雨",
        mood="カジュアル",
        duration_hours=4,
        highlights=["限定醸造クラフトビール", "島唄ライブ", "地元客との交流"],
        ideal_season="オールシーズン",
        ideal_time="夕方〜夜",
        tips=["タクシー配車アプリを入れておくと便利", "ライブバーはチャージ制のため現金を準備"],
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
        ideal_season="春・秋",
        ideal_time="午後",
        tips=["北野坂は坂道が多いので歩きやすい靴で", "人気カフェはピーク前に入店"],
    ),
    Experience(
        city="神戸",
        title="有馬温泉プライベートスパリトリート",
        description=(
            "有馬温泉のラグジュアリーホテルで金泉・銀泉の貸切風呂とスパトリートメントを堪能する極上リトリート。"
        ),
        activity_type="リラクゼーション",
        budget="¥¥¥¥",
        weather="雨",
        mood="ラグジュアリー",
        duration_hours=6,
        highlights=["貸切露天風呂", "ペアルームスパ", "季節の会席ランチ"],
        ideal_season="冬",
        ideal_time="昼〜夕方",
        tips=["宿泊とセットで予約すると特典あり", "温泉後は水分補給を忘れずに"],
        booking_required=True,
    ),
    Experience(
        city="神戸",
        title="ハーバーランド夜景フォトツアー",
        description=(
            "プロカメラマンと一緒に夜のハーバーランドを巡り、ベイエリアの夜景撮影テクニックを学ぶアクティブプラン。"
        ),
        activity_type="アクティビティ",
        budget="¥¥¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=3,
        highlights=["モザイク大観覧車", "明石海峡大橋の遠景", "夜景ポートレート"],
        ideal_season="春〜秋",
        ideal_time="夜",
        tips=["カメラレンタルも可。申し込み時に相談", "雨天延期ポリシーを事前確認"],
        booking_required=True,
    ),
    Experience(
        city="広島",
        title="瀬戸内レモンアイランドサイクリング",
        description=(
            "瀬戸内の島を電動アシスト自転車で巡り、レモン農園で収穫体験と海辺カフェでシーフードを味わう爽快な一日。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=7,
        highlights=["しまなみ海道の絶景", "レモン収穫体験", "海沿いカフェランチ"],
        ideal_season="春〜秋",
        ideal_time="朝〜夕方",
        tips=["フェリーの時刻表を事前確認", "日焼け対策を万全に"],
    ),
    Experience(
        city="広島",
        title="宮島ナイトクルーズと嚴島神社ライトアップ",
        description=(
            "夕暮れの宮島で嚴島神社のライトアップを参拝し、"
            "貸切クルーズで大鳥居のシルエットを海上から眺める特別プラン。"
        ),
        activity_type="クルーズ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["嚴島神社のライトアップ", "貸切クルーズ", "瀬戸内の夜景"],
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["潮位によって参拝時間が変わるので事前に確認", "クルーズ会社に事前予約"],
        booking_required=True,
    ),
    Experience(
        city="広島",
        title="三次ワイナリー見学と里山グランピング",
        description=(
            "広島県北部の三次ワイナリーで醸造見学とテイスティングを楽しみ、"
            "夜は里山グランピング施設で焚き火と星空を満喫するステイケーション。"
        ),
        activity_type="アウトドア",
        budget="¥¥プラス",
        weather="晴れ",
        mood="リラックス",
        duration_hours=24,
        highlights=["ワイナリーツアー", "地元食材のBBQ", "星空観察"],
        ideal_season="春〜秋",
        ideal_time="終日",
        tips=["ドライバーはテイスティングに参加できないため送迎付きプランがおすすめ", "夜は冷えるので厚手の上着を準備"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="ひがし茶屋街着物フォトウォーク",
        description=(
            "伝統工芸師の指導で加賀友禅の着付けを体験し、茶屋街でプロカメラマンが同行するフォトウォーク。"
        ),
        activity_type="カルチャー",
        budget="¥¥¥",
        weather="晴れ",
        mood="伝統",
        duration_hours=4,
        highlights=["加賀友禅の着付け", "古い町並み", "プロの写真データ"],
        ideal_season="春・秋",
        ideal_time="午前〜午後",
        tips=["雨天時はスタジオ撮影に切り替え可", "足袋ソックスを持参すると快適"],
        booking_required=True,
    ),
)


EXPERIENCE_DETAILS: Mapping[str, ExperienceDetail] = {
    "隅田川沿いナイトピクニック": ExperienceDetail(
        neighborhood="浅草・蔵前",
        meeting_point="浅草駅 雷門前",
        access="東京メトロ銀座線/都営浅草線 浅草駅から徒歩3分",
        website="https://www.gotokyo.org/ja/spot/496/index.html",
        contact="墨田区観光協会 問い合わせフォーム",
        attire="夜風対策に薄手のアウターがおすすめ",
        cancellation="荒天の場合は遊歩道が封鎖されることがあります",
        languages=["日本語"],
        suitable_for=["記念日", "夜景好き"],
    ),
    "吉祥寺モーニング散歩と井の頭ボート": ExperienceDetail(
        neighborhood="吉祥寺",
        meeting_point="井の頭恩賜公園ボート場チケット売り場",
        access="JR中央線/京王井の頭線 吉祥寺駅から徒歩5分",
        website="https://www.tokyo-park.or.jp/park/format/index001.html",
        contact="井の頭恩賜公園サービスセンター 0422-47-6900",
        attire="歩きやすいスニーカー推奨",
        cancellation="雨天時はボート営業が休止される場合があります",
        languages=["日本語"],
        suitable_for=["朝活", "自然派カップル"],
    ),
    "神楽坂フレンチと路地裏バー梯子": ExperienceDetail(
        neighborhood="神楽坂",
        meeting_point="神楽坂通り・赤城神社前",
        access="東京メトロ東西線 神楽坂駅1番出口より徒歩2分",
        website="https://kagurazaka.inshokuten.jp/",
        contact="各店舗にてメール予約 (英語対応可)",
        attire="スマートカジュアル",
        cancellation="前日以降のキャンセルはコース料金の50%が発生",
        languages=["日本語", "英語(一部店舗)"],
        suitable_for=["記念日", "ワイン好き"],
    ),
    "嵐山サイクリングと竹林散歩": ExperienceDetail(
        neighborhood="嵐山・嵯峨野",
        meeting_point="嵐山駅前レンタサイクルショップ",
        access="阪急嵐山線 嵐山駅から徒歩1分",
        website="https://www.kyoto-arashiyama.jp/",
        contact="嵐山観光案内所 075-861-0012",
        attire="動きやすい服装とスニーカー",
        cancellation="雨天時はサイクリングを中止し徒歩プランに変更可",
        languages=["日本語", "英語マップあり"],
        suitable_for=["アクティブ派", "初めての京都"],
    ),
    "出町柳モーニングと鴨川ベンチデート": ExperienceDetail(
        neighborhood="出町柳",
        meeting_point="鴨川デルタ 石の飛び石付近",
        access="叡山電鉄・京阪本線 出町柳駅から徒歩3分",
        website="https://kyoto.travel/ja/see-and-do/area/demachiyanagi.html",
        contact="京都市観光協会 インフォメーション",
        attire="川沿いは朝露が残るため防寒と防水の羽織を携帯",
        cancellation="大雨時は川沿いに近づかないよう注意喚起あり",
        languages=["日本語"],
        suitable_for=["朝活", "ピクニック派"],
    ),
    "先斗町おまかせ割烹と祇園ナイトウォーク": ExperienceDetail(
        neighborhood="先斗町・祇園",
        meeting_point="先斗町北詰 鴨川沿い入口",
        access="京阪本線 三条駅から徒歩3分",
        website="https://www.pontochou.jp/",
        contact="割烹店の予約専用ダイヤル (英語対応は事前相談)",
        attire="着物またはジャケットスタイルがおすすめ",
        cancellation="当日キャンセルは100%課金。雨天で川床中止時は店内席に振替",
        languages=["日本語"],
        suitable_for=["大人デート", "和食好き"],
    ),
    "中崎町古着めぐりと路地裏カフェ": ExperienceDetail(
        neighborhood="中崎町",
        meeting_point="大阪メトロ谷町線 中崎町駅2番出口",
        access="大阪メトロ谷町線 中崎町駅から徒歩すぐ",
        website="https://www.explore-nakazakicho.com/",
        contact="中崎町商店会 Instagram DM",
        attire="歩きやすく動きやすいカジュアルファッション",
        cancellation="荒天時は一部店舗が臨時休業となる場合があります",
        languages=["日本語", "英語メニューあり"],
        suitable_for=["カフェ巡り", "カルチャー好き"],
    ),
    "大濠公園モーニングジョグと湖畔カフェ": ExperienceDetail(
        neighborhood="大濠公園",
        meeting_point="大濠公園駅 3 番出口",
        access="福岡市地下鉄空港線 大濠公園駅から徒歩1分",
        website="https://oohori-park.jp/",
        contact="福岡市 大濠公園管理事務所 092-741-2004",
        attire="ランニングウェアと薄手の羽織を持参",
        cancellation="雨天時はランニングステーションが混雑する場合あり",
        languages=["日本語", "英語案内看板あり"],
        suitable_for=["朝活", "ヘルシー志向"],
    ),
    "瀬戸内レモンアイランドサイクリング": ExperienceDetail(
        neighborhood="尾道・生口島",
        meeting_point="尾道駅前しまなみレンタサイクルポート",
        access="JR山陽本線 尾道駅から徒歩1分",
        website="https://shimanami-cycle.or.jp/",
        contact="しまなみレンタサイクル 0848-22-3911",
        attire="汗をかいても乾きやすいサイクリングウェア",
        cancellation="雨天・強風時はフェリーが欠航する場合あり",
        languages=["日本語", "英語ガイドツアーあり"],
        suitable_for=["サイクリング", "アウトドア派"],
    ),

    "お台場サンセットクルーズと夜景ディナー": ExperienceDetail(
        neighborhood="お台場・竹芝",
        meeting_point="日の出桟橋 クルーズ受付カウンター",
        access="ゆりかもめ 竹芝駅から徒歩2分",
        website="https://www.vantean.co.jp/",
        contact="東京ヴァンテアンクルーズ 03-3436-2121",
        attire="スマートカジュアル。船内は冷えるため羽織を携帯",
        cancellation="荒天・強風時は欠航となり全額返金",
        languages=["日本語", "英語メニュー"],
        suitable_for=["記念日", "夜景好き"],
    ),
    "下北沢レコードハンティングとライブハウスナイト": ExperienceDetail(
        neighborhood="下北沢",
        meeting_point="小田急線・京王井の頭線 下北沢駅 中央改札",
        access="小田急線/京王井の頭線 下北沢駅から徒歩1分",
        website="https://www.shimokitazawa.info/",
        contact="ライブハウスへメール予約 (英語対応可)",
        attire="動きやすいカジュアルスタイル",
        cancellation="ライブチケットは当日キャンセル不可",
        languages=["日本語", "英語(一部スタッフ)"],
        suitable_for=["音楽好き", "インディーズファン"],
    ),
    "鞍馬ハイキングと貴船川床ディナー": ExperienceDetail(
        neighborhood="鞍馬・貴船",
        meeting_point="叡山電鉄 鞍馬駅 出口",
        access="叡山電鉄鞍馬線 鞍馬駅から徒歩すぐ",
        website="https://kibune-kyoto.jp/",
        contact="貴船観光会 075-741-4444",
        attire="トレッキングシューズと撥水ジャケット",
        cancellation="川床は雨天・増水時に中止となる場合あり",
        languages=["日本語", "英語パンフレット"],
        suitable_for=["ハイキング", "避暑デート"],
    ),
    "梅田スカイビル空中庭園と夜景ディナー": ExperienceDetail(
        neighborhood="梅田",
        meeting_point="梅田スカイビル 東棟1F エントランス",
        access="JR大阪駅中央北口から徒歩9分",
        website="https://www.skybldg.co.jp/",
        contact="空中庭園展望台 06-6440-3855",
        attire="スマートカジュアル。夜間は屋上が風で冷えるため上着必携",
        cancellation="強風時は屋上がクローズとなる場合あり",
        languages=["日本語", "英語音声ガイド"],
        suitable_for=["夜景撮影", "記念日"],
    ),
    "大通公園イルミネーションと夜景ディナー": ExperienceDetail(
        neighborhood="札幌中心部",
        meeting_point="大通公園2丁目 イルミネーション会場入口",
        access="札幌市営地下鉄 大通駅から徒歩1分",
        website="https://www.sapporo-winter.com/",
        contact="さっぽろホワイトイルミネーション実行委員会",
        attire="防寒性の高いコートと手袋",
        cancellation="暴風雪時は一部エリアが点灯中止となる場合あり",
        languages=["日本語", "英語案内マップ"],
        suitable_for=["冬デート", "夜景好き"],
    ),
    "モエレ沼公園ピクニックとガラスのピラミッド": ExperienceDetail(
        neighborhood="札幌・モエレ沼公園",
        meeting_point="モエレ沼公園 ガラスのピラミッド正面入口",
        access="札幌市営地下鉄東豊線 環状通東駅からバスで25分",
        website="https://moerenumapark.jp/",
        contact="モエレ沼公園管理事務所 011-790-1231",
        attire="芝生に座れるカジュアルウェアと動きやすい靴",
        cancellation="強風・荒天時は屋外施設が閉鎖される場合あり",
        languages=["日本語", "英語パンフレット"],
        suitable_for=["ピクニック", "アート好き"],
    ),
    "柳川川下りと鰻せいろ蒸しランチ": ExperienceDetail(
        neighborhood="柳川",
        meeting_point="西鉄柳川駅改札前 観光案内所",
        access="西鉄天神大牟田線 柳川駅から徒歩5分 (送迎バスあり)",
        website="https://www.yanagawa-net.com/",
        contact="柳川川下り観光事業協同組合 0944-72-6177",
        attire="日差し対策の帽子と動きやすい服装",
        cancellation="強風・荒天時は運航中止となる場合あり",
        languages=["日本語", "英語案内(要予約)"],
        suitable_for=["小旅行", "和食好き"],
    ),
    "宮島ナイトクルーズと嚴島神社ライトアップ": ExperienceDetail(
        neighborhood="宮島",
        meeting_point="宮島桟橋 観光案内所前",
        access="JR宮島口駅からフェリーで10分",
        website="https://www.miyajima.or.jp/",
        contact="宮島観光協会 0829-44-2011",
        attire="歩きやすい靴と羽織。桟橋は夜風が強いことあり",
        cancellation="荒天時はライトアップとクルーズが中止になる場合あり",
        languages=["日本語", "英語案内マップ"],
        suitable_for=["世界遺産", "夜景デート"],
    ),
    "三次ワイナリー見学と里山グランピング": ExperienceDetail(
        neighborhood="広島・三次",
        meeting_point="三次ワイナリー インフォメーション",
        access="JR芸備線 三次駅からタクシーで5分 (送迎バスあり)",
        website="https://miyoshi-winery.co.jp/",
        contact="三次ワイナリー 0824-64-0200",
        attire="動きやすい服装と夜間用の防寒着",
        cancellation="荒天時はグランピングが室内プランへ変更になる場合あり",
        languages=["日本語"],
        suitable_for=["ワイン好き", "星空観賞"],
    ),
    "美ら海水族館と古宇利島サンセットドライブ": ExperienceDetail(
        neighborhood="沖縄本島北部",
        meeting_point="那覇市内レンタカー各社 (送迎あり)",
        access="那覇空港から高速道路利用で約2時間",
        website="https://churaumi.okinawa/",
        contact="沖縄美ら海水族館 0980-48-3748",
        attire="長時間ドライブに適した軽装と日差し対策",
        cancellation="台風接近時は施設閉館や橋の通行止めとなる場合あり",
        languages=["日本語", "英語パンフレット"],
        suitable_for=["ドライブ", "海好き"],
    ),
    "那覇クラフトビールと島唄ライブバー": ExperienceDetail(
        neighborhood="那覇市中心部",
        meeting_point="ゆいレール 牧志駅 北口",
        access="ゆいレール 牧志駅から徒歩5分",
        website="https://www.kokusaidori.or.jp/",
        contact="各店舗SNS (英語対応可)",
        attire="カジュアルで動きやすい服装",
        cancellation="ライブバーは当日キャンセル不可 (要チャージ)",
        languages=["日本語", "英語メニュー"],
        suitable_for=["音楽好き", "はしご酒"],
    ),

}


def _with_detail(exp: Experience) -> Experience:
    detail = EXPERIENCE_DETAILS.get(exp.title)
    if detail and exp.detail != detail:
        return replace(exp, detail=detail)
    if detail is None and exp.detail is not None:
        return replace(exp, detail=None)
    return exp


EXPERIENCES: Tuple[Experience, ...] = tuple(_with_detail(exp) for exp in RAW_EXPERIENCES)
