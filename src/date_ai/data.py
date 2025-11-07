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
    Experience(
        city="東京",
        title="高尾山サンライズトレッキングと温泉朝食",
        description=(
            "始発で高尾山に向かい、日の出を眺めながら山頂でホットコーヒーを楽しむ早朝ハイク。"
            "下山後は麓の温泉で朝食ビュッフェを味わうリフレッシュプラン。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=6,
        highlights=["山頂からの朝日", "森林浴のトレイル", "温泉での朝食ビュッフェ"],
        ideal_season="春〜秋",
        ideal_time="早朝〜午前",
        tips=["ライト付きヘッドランプを持参", "温泉の朝食は事前予約がおすすめ"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="清澄白河ロースタリー巡りとアート散歩",
        description=(
            "清澄白河のロースタリーカフェでスペシャルティコーヒーの飲み比べを楽しみ、"
            "ブルーボトル発祥の街に点在するギャラリーを巡るクリエイティブ散策。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="曇り",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["シングルオリジン飲み比べ", "ミニギャラリー巡り", "深川資料館通りの散歩"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["人気店はモバイルオーダーを活用", "歩きやすいスニーカーで街歩き"],
    ),
    Experience(
        city="東京",
        title="東京湾モーニングクルーズとブランチビュッフェ",
        description=(
            "レインボーブリッジをくぐる東京湾モーニングクルーズで爽やかな海風を浴び、"
            "船内で焼き立てパンが並ぶブランチビュッフェを堪能する爽快な朝。"
        ),
        activity_type="クルーズ",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["朝の東京湾クルーズ", "ライブキッチンのブランチ", "デッキからのフォトスポット"],
        ideal_season="春〜秋",
        ideal_time="午前",
        tips=["出航30分前までに受付", "デッキは風が強いので羽織物を持参"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="神田古書店街とレトロ喫茶読書デート",
        description=(
            "神保町の古書店でお気に入りの本を探し、戦前から続くレトロ喫茶でホットケーキとともに読書を楽しむ知的な午後。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="雨",
        mood="知的",
        duration_hours=3,
        highlights=["稀覯本との出会い", "レトロ喫茶の雰囲気", "こだわりのホットケーキ"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["現金支払いのみの店舗が多いので要注意", "喫茶はピーク前に入店"],
    ),
    Experience(
        city="東京",
        title="代々木公園ピクニックとファーマーズマーケット",
        description=(
            "土日の代々木公園ファーマーズマーケットで旬のオーガニック食材を集め、"
            "芝生でピクニックを楽しむヘルシーな休日プラン。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リラックス",
        duration_hours=4,
        highlights=["ローカル食材の買い出し", "芝生でのピクニック", "青空の下でのライブ演奏"],
        ideal_season="春〜秋",
        ideal_time="午前〜午後",
        tips=["マイバッグとレジャーシートを持参", "人気フードは午前中に完売するので早めに確保"],
    ),
    Experience(
        city="東京",
        title="池袋プラネタリウムとサンシャイン夜景ディナー",
        description=(
            "サンシャインシティ内のプラネタリウムでヒーリングな星空上映を楽しみ、"
            "展望台レストランで夜景を眺めながらディナーを味わうロマンチックナイト。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="雨",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["ヒーリングプラネタリウム", "サンシャイン60の夜景", "季節のコースディナー"],
        ideal_season="オールシーズン",
        ideal_time="夕方〜夜",
        tips=["上映は予約制なので席指定をお早めに", "展望台は入場時間指定チケットがおすすめ"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="赤坂和菓子づくりワークショップと日枝神社参拝",
        description=(
            "赤坂の和菓子教室で練り切り細工のレッスンを受け、出来たてのお菓子を持って日枝神社を参拝する文化体験。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="曇り",
        mood="伝統",
        duration_hours=3,
        highlights=["職人直伝の練り切り", "季節の御朱印", "和モダンな街並み散策"],
        ideal_season="春〜秋",
        ideal_time="午前",
        tips=["エプロンとハンドタオルを持参", "神社の階段はエスカレーターも利用可"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="中目黒ナイトマーケットと目黒川テラスバー",
        description=(
            "中目黒高架下のナイトマーケットでクラフトフードを味わい、"
            "目黒川沿いのテラスバーでカクテルと夜風を楽しむおしゃれな夜散歩。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥",
        weather="晴れ",
        mood="カジュアル",
        duration_hours=4,
        highlights=["期間限定ナイトマーケット", "クラフトカクテル", "イルミネーションテラス"],
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["テラス席は事前予約推奨", "マーケットは電子決済中心"],
    ),
    Experience(
        city="東京",
        title="お茶の水クラシックコンサートと神田川クルーズ",
        description=(
            "御茶ノ水のホールでアフタヌーンの室内楽コンサートを鑑賞し、"
            "神田川を周遊するクルーズで夕暮れの街並みを眺める上質な半日。"
        ),
        activity_type="カルチャー",
        budget="¥¥¥",
        weather="晴れ",
        mood="エレガント",
        duration_hours=5,
        highlights=["生演奏の室内楽", "歴史あるホール", "神田川クルーズ"],
        ideal_season="春・秋",
        ideal_time="午後〜夕方",
        tips=["コンサートチケットは早割を活用", "クルーズは悪天候時欠航あり"],
        booking_required=True,
    ),
    Experience(
        city="東京",
        title="日比谷ミッドタウンテラスシネマとガーデンバー",
        description=(
            "日比谷公園隣接の屋外テラスシネマで話題作を鑑賞し、"
            "上映後はガーデンバーで季節のモクテルを楽しむ都会のリラックスタイム。"
        ),
        activity_type="エンタメ",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["屋外テラスシネマ", "ガーデンライトアップ", "季節のモクテル"],
        ideal_season="初夏〜初秋",
        ideal_time="夜",
        tips=["雨天中止の場合は館内シアターに振替", "ブランケットの貸し出しを活用"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="山手洋館ティールームと港の見える丘公園散策",
        description=(
            "横浜山手の歴史的洋館を巡り、英国風ティールームでアフタヌーンティーを味わった後に"
            "港の見える丘公園でベイブリッジを望むフォトジェニック散歩。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["山手の洋館巡り", "本格アフタヌーンティー", "港が見える展望"],
        ideal_season="春・秋",
        ideal_time="午後",
        tips=["洋館は公開日を事前確認", "ティールームは予約で窓際席確保"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="みなとみらいサンセットクルーズと観覧車ナイトライド",
        description=(
            "夕暮れの横浜港をクルーズで周遊し、赤レンガ倉庫のライトアップを海上から眺めた後に"
            "コスモクロック21へ乗車して夜景を満喫する王道デート。"
        ),
        activity_type="クルーズ",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["横浜港サンセット", "赤レンガの夜景", "観覧車からの360度ビュー"],
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["クルーズは出航30分前集合", "観覧車はWEB前売り券で待ち時間短縮"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="元町ショコラづくりワークショップとナイトカフェ",
        description=(
            "元町のショコラトリーでカカオ豆の焙煎から体験するワークショップに参加し、"
            "仕上げたチョコを持ち寄って夜カフェでペアリングを楽しむスイートな時間。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="スイート",
        duration_hours=3,
        highlights=["ビーントゥバー体験", "ショコラティエ指導", "夜カフェでのチョコペアリング"],
        ideal_season="冬",
        ideal_time="夕方",
        tips=["エプロンと持ち帰り用バッグを用意", "カフェは予約で席確保"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="赤レンガ倉庫スケートリンクとホットワインナイト",
        description=(
            "冬季限定で登場する赤レンガ倉庫の屋外アイススケートリンクで滑り、"
            "ドイツ風マーケットでホットワインとソーセージを味わうウィンターイベント。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="雪",
        mood="ドラマチック",
        duration_hours=3,
        highlights=["ライトアップされたリンク", "期間限定マーケット", "ホットワイン"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["手袋必須のため忘れずに", "リンクは混雑前の夕方がおすすめ"],
    ),
    Experience(
        city="横浜",
        title="新横浜ラーメン博物館食べ歩きと昭和レトロ体験",
        description=(
            "昭和の街並みを再現した新横浜ラーメン博物館で全国のご当地ラーメンを少量ずつ食べ歩き、"
            "駄菓子屋や射的で懐かしさを味わうカジュアルデート。"
        ),
        activity_type="グルメ",
        budget="¥ライト",
        weather="雨",
        mood="カジュアル",
        duration_hours=3,
        highlights=["全国ご当地ラーメン", "昭和レトロの街並み", "駄菓子と射的"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["小サイズのラーメンをシェアして多種類を味わう", "館内は現金のみの店舗もあり"],
    ),
    Experience(
        city="横浜",
        title="八景島シーパラダイス夜間アクアリウムと花火",
        description=(
            "八景島シーパラダイスの夜間限定ナイトアクアリウムを鑑賞し、"
            "イルカショー後に打ち上がる花火を海風と共に楽しむ特別な夜。"
        ),
        activity_type="エンタメ",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=5,
        highlights=["夜のイルカショー", "光のクラゲエリア", "花火スペクタクル"],
        ideal_season="夏",
        ideal_time="夜",
        tips=["帰りのシーサイドライン最終便を確認", "夜は肌寒いので羽織物を持参"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="横浜中華街点心食べ歩きと占い小路めぐり",
        description=(
            "横浜中華街の専門店で出来たて点心を食べ歩き、関帝廟で参拝した後に占い小路で相性鑑定を楽しむ占いデート。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="曇り",
        mood="わくわく",
        duration_hours=3,
        highlights=["手作り小籠包", "関帝廟参拝", "相性占い"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["食べ歩きはシェアで色々楽しむ", "占いは事前予約で待ち時間短縮"],
    ),
    Experience(
        city="横浜",
        title="三溪園早朝写経と日本庭園モーニング",
        description=(
            "三溪園の早朝写経プログラムに参加し、静かな日本庭園で朝粥をいただく心落ち着く一日の始まり。"
        ),
        activity_type="リラクゼーション",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["朝の写経体験", "庭園散策", "精進朝粥"],
        ideal_season="春・秋",
        ideal_time="早朝",
        tips=["受付は開始15分前までに", "動きやすい服装で参加"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="本牧シーサイドBBQとSUPサンセット体験",
        description=(
            "本牧の海辺デッキで手ぶらBBQを楽しんだ後、インストラクター付きのSUPで夕陽に染まる横浜港をクルージングするアクティブプラン。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=5,
        highlights=["海辺の手ぶらBBQ", "SUPレッスン", "サンセットクルージング"],
        ideal_season="夏",
        ideal_time="午後〜夕方",
        tips=["水着とタオルを持参", "SUPは風が強い日は中止の可能性あり"],
        booking_required=True,
    ),
    Experience(
        city="横浜",
        title="黄金町アートスタジオ巡りと高架下ジャズバー",
        description=(
            "黄金町のアートスタジオやギャラリーを巡り、夜は京急高架下のジャズバーで地元ミュージシャンのライブを楽しむアートナイト。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["アーティストスタジオ訪問", "高架下のストリートアート", "生演奏ジャズ"],
        ideal_season="オールシーズン",
        ideal_time="午後〜夜",
        tips=["ギャラリーは営業時間が短いので事前チェック", "ライブチャージの現金を用意"],
    ),
    Experience(
        city="千葉",
        title="幕張ビーチサイクリングと潮風カフェブランチ",
        description=(
            "幕張の海浜幕張公園からレンタサイクルでビーチ沿いを走り、"
            "ゴール地点の海辺カフェで潮風を感じながらブランチを楽しむ爽快プラン。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=3,
        highlights=["海沿いサイクリングロード", "絶景ブランチテラス", "潮風リフレッシュ"],
        ideal_season="春〜秋",
        ideal_time="午前",
        tips=["サイクリングは事前予約で希望車種を確保", "日焼け止めとサングラス必須"],
    ),
    Experience(
        city="千葉",
        title="成田山精進料理ランチと参道まち歩き",
        description=(
            "成田山新勝寺の精進料理を味わい、参道の老舗うなぎ店や和雑貨を巡って歴史の息づく町並みを散策する落ち着いたデート。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="伝統",
        duration_hours=4,
        highlights=["本堂参拝", "精進料理膳", "参道の老舗めぐり"],
        ideal_season="春・秋",
        ideal_time="午前〜午後",
        tips=["参拝は朝の護摩供開始時間に合わせる", "着物レンタル店の予約も人気"],
        booking_required=True,
    ),
    Experience(
        city="千葉",
        title="浦安市舞浜ベイランニングとスパリラクゼーション",
        description=(
            "舞浜のベイサイドランニングコースを朝の海風と共に走り、"
            "ホテル内スパで海水を使ったタラソセラピーを楽しむアクティブリトリート。"
        ),
        activity_type="リラクゼーション",
        budget="¥¥¥",
        weather="晴れ",
        mood="リフレッシュ",
        duration_hours=4,
        highlights=["ベイランニングコース", "ホテルスパ", "タラソセラピー"],
        ideal_season="春〜秋",
        ideal_time="朝〜午前",
        tips=["ラン後のスパ利用は事前予約", "ランニング後の着替えを用意"],
        booking_required=True,
    ),
    Experience(
        city="千葉",
        title="勝浦朝市と漁港食堂ブランチ",
        description=(
            "400年続く勝浦朝市で干物や海鮮を買い物し、漁港直営の食堂で朝獲れの海鮮丼を味わう海の恵み旅。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=4,
        highlights=["勝浦朝市", "漁港直送の海鮮", "港町の散策"],
        ideal_season="春〜秋",
        ideal_time="早朝〜午前",
        tips=["朝市は午前11時までなので早めに訪問", "保冷バッグを持参すると便利"],
    ),
    Experience(
        city="千葉",
        title="館山フラワーパーク温室ピクニック",
        description=(
            "南房総の館山ファミリーパークで季節の花を楽しみ、温室内のカフェで摘みたてハーブティーとスコーンを味わう癒やし時間。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["色とりどりの花畑", "ハーブ収穫体験", "温室カフェ"],
        ideal_season="春",
        ideal_time="午前〜午後",
        tips=["開園直後が写真撮影に最適", "園内は日陰が少ないため帽子を持参"],
    ),
    Experience(
        city="千葉",
        title="佐原小江戸舟めぐりと酒蔵テイスティング",
        description=(
            "小野川沿いに残る佐原の歴史的町並みを舟で巡り、老舗酒蔵で限定の純米酒をテイスティングする情緒ある旅。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="伝統",
        duration_hours=4,
        highlights=["小野川舟めぐり", "重要伝統的建造物群", "酒蔵テイスティング"],
        ideal_season="春・秋",
        ideal_time="午後",
        tips=["舟めぐりは予約制で雨天中止あり", "酒蔵見学は公共交通で訪問"],
        booking_required=True,
    ),
    Experience(
        city="千葉",
        title="銚子犬吠埼灯台サンセットと海鮮ディナー",
        description=(
            "関東最東端の犬吠埼灯台で水平線に沈む夕陽を眺め、灯台下の海鮮食堂で金目鯛料理を味わう海辺の夕暮れプラン。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["犬吠埼灯台の展望", "太平洋サンセット", "金目鯛ディナー"],
        ideal_season="秋",
        ideal_time="夕方",
        tips=["灯台は階段が多いのでスニーカー必須", "日没時刻を事前確認"],
    ),
    Experience(
        city="千葉",
        title="柏クラフトビールタップルームとライブハウスナイト",
        description=(
            "柏駅周辺のクラフトビールタップルームで限定醸造を飲み比べ、夜はライブハウスで地元バンドのステージを楽しむ音楽ナイト。"
        ),
        activity_type="ナイトライフ",
        budget="¥",
        weather="曇り",
        mood="カジュアル",
        duration_hours=4,
        highlights=["限定クラフトビール", "ブルワリー見学", "インディーズライブ"],
        ideal_season="オールシーズン",
        ideal_time="夜",
        tips=["ライブチケットは事前予約", "飲酒後の帰宅手段を確保"],
        booking_required=True,
    ),
    Experience(
        city="千葉",
        title="松戸21世紀の森カヌー体験と森カフェ",
        description=(
            "松戸21世紀の森と広場でインストラクター付きのカヌー体験に参加し、森カフェで無添加スイーツを味わう自然時間。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["静かな池でのカヌー", "季節の森散策", "無添加スイーツ"],
        ideal_season="初夏",
        ideal_time="午前",
        tips=["濡れてもよい服装で参加", "体験は小雨決行だが荒天中止"],
        booking_required=True,
    ),
    Experience(
        city="千葉",
        title="鴨川シーワールド夜間シャチパフォーマンス",
        description=(
            "鴨川シーワールドの夜間開園日に参加し、ライトアップされたスタジアムで迫力のシャチパフォーマンスを鑑賞する特別イベント。"
        ),
        activity_type="エンタメ",
        budget="¥¥",
        weather="晴れ",
        mood="ドラマチック",
        duration_hours=4,
        highlights=["夜間限定シャチショー", "イルミネーション水槽", "海辺の花火"],
        ideal_season="夏",
        ideal_time="夜",
        tips=["濡れる席はポンチョ必須", "帰路のバス最終時刻を確認"],
        booking_required=True,
    ),
    Experience(
        city="千葉",
        title="舞浜ボードウォークサンセットディナー",
        description=(
            "舞浜リゾートのボードウォークで夕暮れ散歩を楽しみ、運河沿いのテラスレストランでシーフードディナーを味わうロマンチックプラン。"
        ),
        activity_type="グルメ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["夕暮れのボードウォーク", "運河を望むテラス席", "シーフードコース"],
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["テラス席は事前リクエスト必須", "日没時間に合わせて予約"],
        booking_required=True,
    ),
    Experience(
        city="埼玉",
        title="川越蔵造り街並みと芋スイーツ食べ歩き",
        description=(
            "小江戸・川越の蔵造りの町並みを散策し、名物の芋スイーツやお団子を食べ歩くレトロな半日旅。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="ノスタルジック",
        duration_hours=4,
        highlights=["蔵造りの町並み", "時の鐘", "芋スイーツ食べ歩き"],
        ideal_season="秋",
        ideal_time="午後",
        tips=["人気店は行列になるのでシェアしながら効率的に", "着物レンタルは事前予約が安心"],
    ),
    Experience(
        city="埼玉",
        title="長瀞ラインくだりと宝登山ロープウェイ",
        description=(
            "秩父・長瀞のラインくだりで荒川の渓流を舟から楽しみ、宝登山ロープウェイで山頂からの絶景を眺める自然満喫コース。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アドベンチャー",
        duration_hours=5,
        highlights=["迫力のラインくだり", "岩畳の散策", "宝登山山頂ビュー"],
        ideal_season="春〜秋",
        ideal_time="午前〜午後",
        tips=["濡れてもいい服装で参加", "川の水量次第でコース変更あり"],
        booking_required=True,
    ),
    Experience(
        city="埼玉",
        title="所沢航空記念公園ピクニックとカフェロースタリー",
        description=(
            "所沢航空記念公園で飛行機展示を見学しながら芝生でピクニックを楽しみ、公園内のロースタリーカフェでスペシャルティコーヒーを味わう休日。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["航空発祥記念館", "広々とした芝生", "自家焙煎コーヒー"],
        ideal_season="春〜秋",
        ideal_time="午後",
        tips=["テントやタープの持ち込みは指定エリアのみ", "カフェは週末混雑のため整理券制"],
    ),
    Experience(
        city="埼玉",
        title="飯能メッツァ北欧サウナと湖畔カヌー",
        description=(
            "北欧の世界観が広がるメッツァヴィレッジで湖畔カヌーを楽しみ、併設のアウトドアサウナでロウリュと外気浴を堪能するリトリート体験。"
        ),
        activity_type="リラクゼーション",
        budget="¥¥¥",
        weather="晴れ",
        mood="リフレッシュ",
        duration_hours=5,
        highlights=["湖上カヌー", "アウトドアサウナ", "北欧マーケット"],
        ideal_season="初夏〜初秋",
        ideal_time="午後",
        tips=["サウナ利用は水着必須", "カヌー体験は風が強いと中止の可能性あり"],
        booking_required=True,
    ),
    Experience(
        city="埼玉",
        title="熊谷星川夜灯と川沿いカフェ",
        description=(
            "熊谷市の星川通りに並ぶ提灯が灯る夜灯イベントを散策し、川沿いのカフェバーで地元クラフトジンを味わう秋の夜散歩。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["星川夜灯の提灯", "熊谷桜堤の夜景", "クラフトジン"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["イベント開催日は混雑するため公共交通機関で", "夜は冷え込むので防寒を"],
    ),
    Experience(
        city="埼玉",
        title="さいたま新都心イルミネーションとアリーナコンサート",
        description=(
            "冬のけやきひろばイルミネーションを散歩し、さいたまスーパーアリーナで開催されるコンサートを楽しむ華やかな夜。"
        ),
        activity_type="エンタメ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ドラマチック",
        duration_hours=4,
        highlights=["けやきひろばイルミネーション", "アリーナライブ", "駅直結の利便性"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["コンサートチケットは早めの確保", "イルミエリアは防寒対策を万全に"],
        booking_required=True,
    ),
    Experience(
        city="埼玉",
        title="三峯神社早朝参拝と雲海ウォッチング",
        description=(
            "標高1100mの三峯神社で早朝参拝を行い、雲海テラスからの幻想的な眺めを楽しんだ後に温泉で体を温める神秘的な旅。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="スピリチュアル",
        duration_hours=8,
        highlights=["早朝参拝", "雲海ビュー", "温泉休憩"],
        ideal_season="晩秋",
        ideal_time="早朝",
        tips=["マイカー規制日に注意", "防寒着と歩きやすい靴を準備"],
        booking_required=True,
    ),
    Experience(
        city="埼玉",
        title="越生梅林ライトアップとキャンドルナイト",
        description=(
            "越生梅林の開花時期に合わせて開催されるライトアップを鑑賞し、キャンドルナイトの幻想的な雰囲気を楽しむ季節限定イベント。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["ライトアップされた梅林", "香り豊かな夜散歩", "甘酒のふるまい"],
        ideal_season="早春",
        ideal_time="夜",
        tips=["夜は冷えるのでカイロを用意", "ライトアップ日は混雑するため早めの入場"],
    ),
    Experience(
        city="埼玉",
        title="川口鋳物体験とアートファクトリー見学",
        description=(
            "鋳物の街・川口で鋳造工房のワークショップに参加し、隣接するアートファクトリーで現代アート展示を楽しむクラフトデート。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["鋳物製作体験", "職人の工房見学", "アート展示"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["工房体験は予約制で安全靴の貸出あり", "作品は後日郵送の場合あり"],
        booking_required=True,
    ),
    Experience(
        city="埼玉",
        title="浦和うなぎ食べ比べと調神社参拝",
        description=(
            "浦和の老舗うなぎ店で白焼きと蒲焼きを食べ比べ、月待信仰で有名な調神社を参拝するグルメ＆カルチャーコース。"
        ),
        activity_type="グルメ",
        budget="¥¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["老舗のうなぎ", "食べ比べコース", "調神社のうさぎ守"],
        ideal_season="夏",
        ideal_time="昼",
        tips=["人気店は整理券制なので開店前に到着", "神社は階段が少なく歩きやすい"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="名古屋モーニング巡りと大須商店街散策",
        description=(
            "名古屋駅周辺の老舗喫茶でボリュームたっぷりのモーニングを楽しみ、大須商店街で古着や雑貨を巡る活気ある朝の散策。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="カジュアル",
        duration_hours=4,
        highlights=["名古屋モーニング", "大須商店街の食べ歩き", "万松寺通りのアーケード"],
        ideal_season="オールシーズン",
        ideal_time="朝〜午前",
        tips=["人気喫茶は開店前に並ぶのが確実", "アーケード内は現金のみの店舗もあり"],
    ),
    Experience(
        city="名古屋",
        title="熱田神宮早朝参拝と宮きしめんブレックファスト",
        description=(
            "朝の澄んだ空気の中で熱田神宮を参拝し、境内の宮きしめんで出汁の効いた朝食を味わう清々しいスタート。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="スピリチュアル",
        duration_hours=2,
        highlights=["熱田神宮参拝", "大楠のパワースポット", "名物宮きしめん"],
        ideal_season="春",
        ideal_time="早朝",
        tips=["朝7時台は人が少なく神聖な雰囲気", "境内は歩きやすい靴で"],
    ),
    Experience(
        city="名古屋",
        title="名古屋港ガーデンふ頭ナイトクルーズ",
        description=(
            "名古屋港ガーデンふ頭から出航するナイトクルーズで港の夜景を眺め、船上でシェフ特製のコース料理とジャズライブを楽しむ特別な夜。"
        ),
        activity_type="クルーズ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["港の夜景", "船上ジャズライブ", "コースディナー"],
        ideal_season="春〜秋",
        ideal_time="夜",
        tips=["ドレスコードはスマートカジュアル", "強風時はデッキが閉鎖されることあり"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="栄スカイデッキシネマとミッドランドバー",
        description=(
            "栄の屋外スカイデッキで開催される星空シネマを鑑賞し、上映後はミッドランドスクエアのバーで夜景カクテルを楽しむ都会の夜遊び。"
        ),
        activity_type="エンタメ",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["屋外シネマ", "栄の夜景", "シグネチャーカクテル"],
        ideal_season="初夏〜初秋",
        ideal_time="夜",
        tips=["雨天時は屋内シアターに振替", "夜風対策に薄手のブランケットを"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="瀬戸焼アトリエでのろくろ体験と窯元ランチ",
        description=(
            "瀬戸市の陶芸アトリエで電動ろくろを体験し、窯元が営むカフェで器に合わせた季節のランチを楽しむクラフトデート。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["陶芸ろくろ体験", "釉薬選び", "窯元カフェランチ"],
        ideal_season="オールシーズン",
        ideal_time="午前〜午後",
        tips=["作品は焼成に1か月ほどかかる", "エプロンとタオルを持参"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="豊田市美術館ナイトミュージアムと庭園ライトアップ",
        description=(
            "金曜夜限定の豊田市美術館ナイトミュージアムで現代アートを鑑賞し、ライトアップされた庭園を散策する静かなアートナイト。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="知的",
        duration_hours=3,
        highlights=["ナイトミュージアム", "水盤のライトアップ", "ミュージアムカフェ"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["金曜夜のみ開館延長", "館内は冷えるので羽織物を"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="犬山城下町着物さんぽと城下スイーツ",
        description=(
            "犬山城下町で着物レンタルをして古民家カフェや団子店を巡り、木曽川沿いの茶屋で城を望む甘味を楽しむレトロデート。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["犬山城下町散策", "着物レンタル", "城下スイーツ"],
        ideal_season="春",
        ideal_time="午後",
        tips=["着物レンタルは事前予約", "坂道が多いので歩きやすい草履を選ぶ"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="知多半島ワイナリー見学とオーシャンテラス",
        description=(
            "名古屋から電車で行ける知多半島のワイナリーで畑見学とテイスティングを行い、海が見えるテラスでペアリングコースを味わう大人の小旅行。"
        ),
        activity_type="グルメ",
        budget="¥¥プラス",
        weather="晴れ",
        mood="エレガント",
        duration_hours=6,
        highlights=["ワイナリー見学", "ソムリエのテイスティング", "オーシャンビューランチ"],
        ideal_season="初夏",
        ideal_time="昼",
        tips=["公共交通利用で訪問", "飲酒後の運転は厳禁"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="名古屋城庭園茶会と金シャチ横丁ディナー",
        description=(
            "名古屋城の二之丸庭園で開かれる茶会に参加し、夕暮れは金シャチ横丁で名古屋めしを味わう文化体験プラン。"
        ),
        activity_type="カルチャー",
        budget="¥¥¥",
        weather="晴れ",
        mood="伝統",
        duration_hours=4,
        highlights=["二之丸庭園の茶会", "呈茶体験", "金シャチ横丁の名古屋めし"],
        ideal_season="秋",
        ideal_time="午後〜夜",
        tips=["茶会は定員制のため早めの申し込み", "金シャチ横丁は混雑時間を避ける"],
        booking_required=True,
    ),
    Experience(
        city="名古屋",
        title="徳川園紅葉ライトアップとミュージアムナイト",
        description=(
            "徳川園の紅葉ライトアップを庭園の回遊式散策で楽しみ、徳川美術館の夜間特別開館で刀剣コレクションを鑑賞する雅な夜。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["紅葉ライトアップ", "池泉回遊式庭園", "徳川美術館の夜間展示"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["ライトアップ期間は入場制限があるため前売り券を", "庭園内は段差が多いので歩きやすい靴で"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="三保の松原サンライズヨガと海辺カフェ",
        description=(
            "世界文化遺産・三保の松原で富士山を望みながらサンライズヨガを行い、海辺のカフェでしらすトーストの朝食をいただく爽やかな朝。"
        ),
        activity_type="リラクゼーション",
        budget="¥¥",
        weather="晴れ",
        mood="リフレッシュ",
        duration_hours=3,
        highlights=["富士山ビューのヨガ", "松林の散策", "海辺カフェの朝食"],
        ideal_season="春〜秋",
        ideal_time="早朝",
        tips=["マットはレンタル可能だが事前予約推奨", "朝露で足元が濡れるためタオルを持参"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="清水港まぐろセリ見学と寿司ブレックファスト",
        description=(
            "早朝の清水魚市場でまぐろのセリを見学し、市場内の寿司店で朝獲れネタの握りを味わう海の朝活。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=3,
        highlights=["まぐろセリ見学", "市場寿司", "港の朝景"],
        ideal_season="冬",
        ideal_time="早朝",
        tips=["セリ見学は人数制限があるため事前申し込み必須", "冷えるので防寒具を持参"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="修善寺温泉竹林の小径と足湯めぐり",
        description=(
            "修善寺温泉の竹林の小径を散策し、足湯カフェでゆずドリンクを楽しみながら温泉街の風情を味わう癒やし散歩。"
        ),
        activity_type="リラクゼーション",
        budget="¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["竹林の小径", "足湯カフェ", "温泉街スイーツ"],
        ideal_season="秋",
        ideal_time="午後",
        tips=["足湯タオルを持参", "竹林は夜間ライトアップも開催される日あり"],
    ),
    Experience(
        city="静岡",
        title="浜名湖サイクリングと湖畔うなぎランチ",
        description=(
            "浜名湖を一望するサイクリングロードを電動アシストで走り、湖畔の老舗で炭火うなぎを味わうアクティブグルメ旅。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=5,
        highlights=["湖畔サイクリング", "展望スポット", "炭火うなぎ"],
        ideal_season="春〜秋",
        ideal_time="午前〜午後",
        tips=["サイクリングはレンタル予約必須", "湖畔は風が強いのでウインドブレーカーを"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="沼津港深海水族館ナイトツアーと海鮮丼",
        description=(
            "沼津港深海水族館の夜間ツアーでダイオウグソクムシなど深海生物を観察し、港の食堂で深海魚丼を味わうディープな夜。"
        ),
        activity_type="エンタメ",
        budget="¥¥",
        weather="雨",
        mood="好奇心",
        duration_hours=4,
        highlights=["夜の深海水族館", "専門ガイドの解説", "深海魚丼"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["夜間ツアーは限定開催なので公式サイトで日程確認", "食堂は早めにラストオーダーをチェック"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="御殿場アウトレットサンセットショッピング",
        description=(
            "御殿場プレミアム・アウトレットで夕方の富士山ビューを楽しみながらショッピングし、イルミネーションと共にダイニングで食事を味わうプラン。"
        ),
        activity_type="ショッピング",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=5,
        highlights=["富士山ビュー", "サンセットイルミネーション", "アウトレットディナー"],
        ideal_season="冬",
        ideal_time="午後〜夜",
        tips=["富士山が見える西エリアを狙う", "夜は冷えるので厚手の上着を"],
    ),
    Experience(
        city="静岡",
        title="熱海花火クルーズと温泉リゾートステイ",
        description=(
            "熱海湾で打ち上がる花火大会をクルーズ船の特等席から鑑賞し、終了後は温泉リゾートで海を眺めながら露天風呂に浸かる贅沢な夜。"
        ),
        activity_type="クルーズ",
        budget="¥¥¥¥",
        weather="晴れ",
        mood="ドラマチック",
        duration_hours=6,
        highlights=["熱海湾花火", "クルーズ船の特等席", "オーシャンビュー温泉"],
        ideal_season="夏",
        ideal_time="夜",
        tips=["花火開催日は宿泊プランが早く埋まるため早めに予約", "花火の煙が風向きで流れるので風予報をチェック"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="焼津かつお節工場見学と出汁ワークショップ",
        description=(
            "焼津のかつお節工場で削りたての香りを体験し、出汁ソムリエによる味比べワークショップに参加して旨味を学ぶ食文化ツアー。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="知的",
        duration_hours=3,
        highlights=["かつお節製造見学", "出汁テイスティング", "削り体験"],
        ideal_season="オールシーズン",
        ideal_time="午前",
        tips=["見学は衛生帽着用のためヘアスタイルに注意", "香りが服に残るので気になる方は着替えを"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="掛川茶畑サンセットと茶室ティーセレモニー",
        description=(
            "掛川の茶畑で夕暮れに染まる段々畑を眺め、茶匠による煎茶の淹れ方講座と茶室での呈茶を体験するグリーンティーツアー。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["茶畑散策", "煎茶の淹れ方講座", "茶室での呈茶"],
        ideal_season="初夏",
        ideal_time="夕方",
        tips=["茶畑は坂道が多いのでスニーカー必須", "夕暮れ時は虫除け対策を"],
        booking_required=True,
    ),
    Experience(
        city="静岡",
        title="富士宮浅間神社と湧玉池カフェテラス",
        description=(
            "富士山本宮浅間大社で参拝し、湧玉池のほとりで名物富士宮やきそばと地ビールを楽しむ富士山の恵みプラン。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="スピリチュアル",
        duration_hours=3,
        highlights=["浅間大社参拝", "湧玉池の清流", "富士宮やきそば"],
        ideal_season="春",
        ideal_time="午後",
        tips=["境内は水辺が多いので滑りにくい靴で", "やきそば店は行列のため時間に余裕を"],
    ),
    Experience(
        city="金沢",
        title="兼六園雪吊りライトアップと鼓門イルミ",
        description=(
            "冬の兼六園で雪吊りが幻想的にライトアップされる夜間開園を散策し、金沢駅鼓門のイルミネーションを眺めるロマンチックな夜。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雪",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["雪吊りライトアップ", "霞ヶ池の水鏡", "鼓門イルミネーション"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["足元が滑りやすいので滑り止め付きブーツ推奨", "ライトアップ日は入園整理券制"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="近江町市場朝ごはんと九谷焼カフェ",
        description=(
            "近江町市場で旬の海鮮を使った海鮮丼を朝食にいただき、九谷焼の器でドリンクを提供するギャラリーカフェでゆったり過ごす朝活。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=3,
        highlights=["市場の海鮮丼", "加賀野菜", "九谷焼の器カフェ"],
        ideal_season="春",
        ideal_time="朝",
        tips=["市場は朝9時までが比較的空いている", "現金のみの店舗が多いので小銭を用意"],
    ),
    Experience(
        city="金沢",
        title="金沢21世紀美術館ナイトプログラム",
        description=(
            "金沢21世紀美術館の夜間プログラムで現代アートのガイドツアーに参加し、ミュージアムショップで限定グッズを楽しむ知的な夜。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=3,
        highlights=["夜間ガイドツアー", "レアンドロのプール", "ミュージアムカフェ"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["夜間プログラムは事前申し込み制", "館内は冷えるので羽織物を"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="ひゃくまん穀おにぎり作りと農家ランチ",
        description=(
            "金沢近郊の農家でブランド米・ひゃくまん穀のおにぎり作りを体験し、旬の加賀野菜を使ったランチを味わうローカルフード体験。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=4,
        highlights=["ひゃくまん穀おにぎり", "農園見学", "加賀野菜ランチ"],
        ideal_season="初夏",
        ideal_time="午前〜午後",
        tips=["農作業体験があるため動きやすい服装で", "収穫体験は天候で変動"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="主計町茶屋街夕涼みと川床カフェ",
        description=(
            "夕暮れの主計町茶屋街をそぞろ歩きし、浅野川沿いに夏季限定で設けられる川床カフェで地酒とスイーツを楽しむ涼やかな時間。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["主計町茶屋街の灯り", "川床カフェ", "地酒カクテル"],
        ideal_season="夏",
        ideal_time="夕方〜夜",
        tips=["川床は雨天中止", "蚊除け対策を忘れずに"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="金箔貼りアクセサリーワークショップ",
        description=(
            "金沢の金箔工房でアクセサリーに金箔を貼る体験を行い、完成した作品を記念に持ち帰るクラフトプラン。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=2,
        highlights=["金箔貼り体験", "熟練職人のレクチャー", "オリジナルアクセサリー"],
        ideal_season="オールシーズン",
        ideal_time="午後",
        tips=["細かい作業のため爪は短く整えて参加", "作品は当日持ち帰り可能"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="金沢港クルーズターミナル夜景散歩",
        description=(
            "金沢港クルーズターミナルの展望デッキから港の夜景を眺め、併設カフェで加賀棒茶ラテを楽しむ静かなシーサイドナイト。"
        ),
        activity_type="ナイトライフ",
        budget="¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=2,
        highlights=["港の夜景", "ライトアップされたクルーズ船", "加賀棒茶ラテ"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["展望デッキは風が強いので羽織物を", "カフェのラストオーダーを事前確認"],
    ),
    Experience(
        city="金沢",
        title="加賀友禅染め体験と茶屋街フォト散歩",
        description=(
            "加賀友禅工房で染色体験を行い、自作の手ぬぐいを持ってひがし茶屋街をフォト散歩する色彩豊かなプラン。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="曇り",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["加賀友禅染め体験", "工房見学", "茶屋街フォトスポット"],
        ideal_season="春",
        ideal_time="午後",
        tips=["染料が飛ぶことがあるのでエプロン必須", "作品は乾燥に時間がかかるため翌日受け取りも可"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="片町バーテンダーツアーと地元カクテル",
        description=(
            "片町の老舗バーを巡るバーテンダーツアーで、地元食材を使ったオリジナルカクテルを飲み比べる大人の夜遊び。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="雨",
        mood="エレガント",
        duration_hours=4,
        highlights=["バーテンダーのシェイカー技", "地元食材カクテル", "会員制バーの雰囲気"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["ツアーは少人数制で要予約", "飲み過ぎに注意しタクシー手配を"],
        booking_required=True,
    ),
    Experience(
        city="金沢",
        title="金石港朝市と海鮮炙り体験",
        description=(
            "金石港朝市で新鮮な魚介を選び、その場で炙り焼きにして味わう活気あふれる朝の市場体験。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=3,
        highlights=["金石港朝市", "炙り体験", "漁師トーク"],
        ideal_season="夏",
        ideal_time="朝",
        tips=["朝市は午前9時頃に終了", "炙り場は煙が出るので匂いが気になる服は避ける"],
    ),
    Experience(
        city="仙台",
        title="仙台朝市モーニングと喫茶レトロ",
        description=(
            "仙台朝市で旬の海鮮を使ったお惣菜をテイクアウトし、老舗喫茶で昭和レトロなモーニングセットを楽しむ地元密着コース。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=3,
        highlights=["仙台朝市での買い物", "老舗喫茶モーニング", "地元の交流"],
        ideal_season="春",
        ideal_time="朝",
        tips=["朝市は8時台が品揃え豊富", "喫茶店はモーニング数量限定"],
    ),
    Experience(
        city="仙台",
        title="松島湾サンセットクルーズとカキ小屋ディナー",
        description=(
            "日本三景・松島湾を夕暮れのクルーズで巡り、港のカキ小屋で焼きがきを味わう海の恵みプラン。"
        ),
        activity_type="クルーズ",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["松島湾の島々", "サンセットクルーズ", "カキ小屋食べ放題"],
        ideal_season="秋",
        ideal_time="夕方〜夜",
        tips=["クルーズは潮位により航路変更あり", "カキ小屋は予約で席確保"],
        booking_required=True,
    ),
    Experience(
        city="仙台",
        title="定禅寺ストリートジャズとイルミネーション",
        description=(
            "定禅寺通りで開催されるストリートジャズフェスティバルを楽しみ、夜は光のページェントイルミネーションを散策する音楽と光の一日。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="わくわく",
        duration_hours=5,
        highlights=["路上ジャズライブ", "杜の都のケヤキ並木", "冬のイルミネーション"],
        ideal_season="冬",
        ideal_time="午後〜夜",
        tips=["防寒具をしっかり", "人気ステージは早めに場所取り"],
    ),
    Experience(
        city="仙台",
        title="秋保温泉足湯カフェと磊々峡ライトアップ",
        description=(
            "秋保温泉街の足湯カフェで温まり、夜は磊々峡のライトアップを散策する癒やしの温泉リトリート。"
        ),
        activity_type="リラクゼーション",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=4,
        highlights=["足湯カフェ", "秋保温泉街", "磊々峡ライトアップ"],
        ideal_season="秋",
        ideal_time="夕方〜夜",
        tips=["足湯タオルを持参", "ライトアップ日は混雑するためバス時刻を確認"],
        booking_required=True,
    ),
    Experience(
        city="仙台",
        title="蔵王御釜トレッキングと天空カフェ",
        description=(
            "蔵王エコーラインをドライブし、御釜展望台からの眺望を楽しんだ後に山頂カフェで限定スイーツを味わう絶景トレッキング。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アドベンチャー",
        duration_hours=6,
        highlights=["御釜のエメラルドグリーン", "高山植物", "天空カフェスイーツ"],
        ideal_season="夏",
        ideal_time="午前〜午後",
        tips=["火山活動により立入規制がある場合あり", "標高が高いので防寒着必須"],
        booking_required=True,
    ),
    Experience(
        city="仙台",
        title="仙台クラフトビールはしごと路地裏ライブ",
        description=(
            "仙台駅周辺のクラフトビールバーを巡り、夜は路地裏のライブハウスでインディーズバンドの演奏を楽しむナイトカルチャー。"
        ),
        activity_type="ナイトライフ",
        budget="¥",
        weather="雨",
        mood="カジュアル",
        duration_hours=4,
        highlights=["地元ブルワリーのビール", "テイスティングフライト", "路地裏ライブ"],
        ideal_season="オールシーズン",
        ideal_time="夜",
        tips=["ライブチケットは事前購入", "終電時間をチェック"],
    ),
    Experience(
        city="仙台",
        title="七夕飾りワークショップと星空プラネタリウム",
        description=(
            "仙台七夕祭りの飾り作りを体験できるワークショップに参加し、夜は天文台のプラネタリウムで星空解説を楽しむロマンチックナイト。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["七夕飾り製作", "仙台天文台", "星空プラネタリウム"],
        ideal_season="夏",
        ideal_time="夕方〜夜",
        tips=["ワークショップは事前予約制", "天文台へは車またはバスで移動"],
        booking_required=True,
    ),
    Experience(
        city="仙台",
        title="ニッカ宮城峡蒸溜所テイスティングツアー",
        description=(
            "青葉山の自然に囲まれたニッカ宮城峡蒸溜所で製造工程を学び、限定ウイスキーのテイスティングを楽しむ大人の学び旅。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="曇り",
        mood="エレガント",
        duration_hours=4,
        highlights=["蒸溜所見学", "シングルモルトテイスティング", "渓谷の自然散策"],
        ideal_season="春",
        ideal_time="午前",
        tips=["試飲があるため公共交通または送迎バス利用", "人気のため早めの予約が必要"],
        booking_required=True,
    ),
    Experience(
        city="仙台",
        title="青葉山ナイトハイクと夜景テラス",
        description=(
            "青葉山公園をナイトハイクで歩き、山頂の展望テラスから仙台の街明かりを眺めるアクティブな夜散歩。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="アドベンチャー",
        duration_hours=3,
        highlights=["ナイトハイク", "展望テラス", "杜の都の夜景"],
        ideal_season="夏",
        ideal_time="夜",
        tips=["足元を照らすヘッドライト必須", "クマ鈴を携帯"],
    ),
    Experience(
        city="福岡",
        title="博多屋台はしごと中洲リバークルーズ",
        description=(
            "中洲のリバークルーズで那珂川の夜景を楽しんだ後、博多屋台をはしごしてラーメンと焼きラーメンを味わうナイトグルメツアー。"
        ),
        activity_type="ナイトライフ",
        budget="¥",
        weather="晴れ",
        mood="わくわく",
        duration_hours=4,
        highlights=["那珂川ナイトクルーズ", "屋台ラーメン", "地元の交流"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["屋台は現金のみの店が多い", "クルーズは雨天欠航あり"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="大濠公園サンライズジョグと湖畔カフェ",
        description=(
            "大濠公園のランニングコースを朝日と共にジョギングし、湖畔カフェでヘルシーボウルとコールドプレスジュースを楽しむ爽やかな朝。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リフレッシュ",
        duration_hours=2,
        highlights=["湖畔の朝焼け", "ランニングコース", "ヘルシーカフェ"],
        ideal_season="春",
        ideal_time="早朝",
        tips=["ラン後の着替えを用意", "カフェはモバイルオーダー対応"],
    ),
    Experience(
        city="福岡",
        title="糸島サンセットビーチと手ぶらBBQ",
        description=(
            "糸島半島のサンセットビーチでビーチヨガを楽しみ、手ぶらBBQで地元野菜とシーフードを味わうリゾート気分デート。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=5,
        highlights=["糸島サンセット", "ビーチヨガ", "手ぶらBBQ"],
        ideal_season="夏",
        ideal_time="午後〜夕方",
        tips=["送迎付きプランが便利", "日焼け止めとサンダルを持参"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="柳川川下りとうなぎせいろ蒸しランチ",
        description=(
            "柳川の掘割を船頭の唄を聞きながら川下りし、老舗で名物うなぎのせいろ蒸しをいただく水郷めぐり。"
        ),
        activity_type="クルーズ",
        budget="¥¥",
        weather="晴れ",
        mood="リラックス",
        duration_hours=4,
        highlights=["川下り", "水郷の風景", "うなぎせいろ蒸し"],
        ideal_season="春",
        ideal_time="午前〜午後",
        tips=["日差し対策に帽子を持参", "川下りは雨天時に運休する場合あり"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="門司港レトロ夜景散歩と焼きカレー",
        description=(
            "門司港レトロ地区でライトアップされた建物を散策し、老舗喫茶で名物焼きカレーを味わうノスタルジックナイト。"
        ),
        activity_type="ナイトライフ",
        budget="¥",
        weather="晴れ",
        mood="ノスタルジック",
        duration_hours=3,
        highlights=["門司港レトロの夜景", "ブルーウィングもじ", "焼きカレー"],
        ideal_season="秋",
        ideal_time="夜",
        tips=["観光列車の時間に合わせて訪れるとロマンチック", "喫茶はラストオーダーが早め"],
    ),
    Experience(
        city="福岡",
        title="太宰府朝詣りと梅ヶ枝餅食べ歩き",
        description=(
            "朝の静かな太宰府天満宮を参拝し、参道で焼きたての梅ヶ枝餅を食べ比べるパワースポット巡り。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="スピリチュアル",
        duration_hours=3,
        highlights=["太宰府天満宮参拝", "朝の参道散策", "梅ヶ枝餅食べ比べ"],
        ideal_season="春",
        ideal_time="朝",
        tips=["開門直後は人が少なく写真撮影に最適", "参道は石畳なので歩きやすい靴で"],
    ),
    Experience(
        city="福岡",
        title="福岡市科学館プラネタリウムと六本松ディナー",
        description=(
            "福岡市科学館の最新プラネタリウムで星空を鑑賞し、六本松エリアのビストロで地元食材を使ったコースディナーを楽しむ知的な夜。"
        ),
        activity_type="エンタメ",
        budget="¥¥",
        weather="雨",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["ドームシアター", "星空解説", "地元食材ビストロ"],
        ideal_season="オールシーズン",
        ideal_time="夕方〜夜",
        tips=["プラネタリウムは人気回は完売するので事前予約", "ディナーはコース予約でスムーズ"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="博多旧市街寺社巡りと和菓子づくり",
        description=(
            "博多旧市街の櫛田神社と東長寺を参拝し、町家で和菓子づくり体験に参加する文化散策。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="曇り",
        mood="伝統",
        duration_hours=4,
        highlights=["櫛田神社", "博多千年門", "和菓子レッスン"],
        ideal_season="秋",
        ideal_time="午後",
        tips=["和菓子体験は予約制", "寺社は御朱印帳をお忘れなく"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="九州国立博物館ナイトミュージアムと光の回廊",
        description=(
            "九州国立博物館の夜間開館で特別展示を鑑賞し、太宰府天満宮へ続く光の回廊を歩く幻想的な夜。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="ドラマチック",
        duration_hours=3,
        highlights=["ナイトミュージアム", "光の回廊", "太宰府の夜景"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["夜間開館日は公式サイトで確認", "回廊は坂道があるため歩きやすい靴で"],
        booking_required=True,
    ),
    Experience(
        city="福岡",
        title="福岡タワー夜景ディナーとビーチイルミ",
        description=(
            "福岡タワーの展望レストランで夜景を眺めながらコースディナーを楽しみ、百道浜のビーチイルミネーションを散策するシーサイドプラン。"
        ),
        activity_type="ナイトライフ",
        budget="¥¥¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=4,
        highlights=["福岡タワーからの夜景", "展望レストラン", "百道浜イルミネーション"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["窓際席は事前リクエスト", "ビーチ沿いは風が強いのでコート必須"],
        booking_required=True,
    ),
    Experience(
        city="札幌",
        title="札幌中央卸売市場朝ごはんと場外散歩",
        description=(
            "札幌中央卸売市場場外市場で鮭いくら丼の朝食を楽しみ、海産物店やローカルベーカリーを巡る活気あるモーニング。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=3,
        highlights=["鮭いくら丼", "場外市場の買い物", "ローカルベーカリー"],
        ideal_season="夏",
        ideal_time="朝",
        tips=["市場は7時台が狙い目", "保冷バッグを持参"],
    ),
    Experience(
        city="札幌",
        title="円山公園モーニングピクニックと北海道神宮参拝",
        description=(
            "円山公園の森林浴トレイルを散歩し、北海道神宮で参拝後にベーカリーで買ったパンを芝生で楽しむ清々しい午前プラン。"
        ),
        activity_type="アウトドア",
        budget="¥ライト",
        weather="晴れ",
        mood="リラックス",
        duration_hours=3,
        highlights=["円山公園の緑", "北海道神宮参拝", "ベーカリーピクニック"],
        ideal_season="春",
        ideal_time="午前",
        tips=["熊鈴を携帯すると安心", "ベーカリーは午前中に売り切れることあり"],
    ),
    Experience(
        city="札幌",
        title="モエレ沼公園ガラスピラミッドサンセット",
        description=(
            "イサム・ノグチ設計のモエレ沼公園でレンタサイクルを楽しみ、ガラスのピラミッドから夕焼けを眺めるアートと自然の融合体験。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["レンタサイクル", "ガラスのピラミッド", "夕焼けの景色"],
        ideal_season="夏",
        ideal_time="午後〜夕方",
        tips=["サイクルは数量限定なので早めに確保", "日没後は冷えるのでジャケット必須"],
    ),
    Experience(
        city="札幌",
        title="札幌芸術の森陶芸体験と森のレストラン",
        description=(
            "札幌芸術の森工房で陶芸体験に参加し、森のレストランで地産地消のランチを味わうクラフト時間。"
        ),
        activity_type="カルチャー",
        budget="¥¥",
        weather="雨",
        mood="クリエイティブ",
        duration_hours=4,
        highlights=["陶芸体験", "工房見学", "森のレストランランチ"],
        ideal_season="オールシーズン",
        ideal_time="午前〜午後",
        tips=["作品は焼成に数週間かかる", "エプロンとハンドタオルを持参"],
        booking_required=True,
    ),
    Experience(
        city="札幌",
        title="サッポロビール園ナイトツアーとジンギスカン",
        description=(
            "サッポロビール園の夜間ガイドツアーで醸造の歴史を学び、レンガ造りのホールでジンギスカン食べ放題を楽しむ王道グルメ。"
        ),
        activity_type="グルメ",
        budget="¥¥",
        weather="雪",
        mood="カジュアル",
        duration_hours=4,
        highlights=["夜間ビールツアー", "レンガ造りホール", "ジンギスカン"],
        ideal_season="冬",
        ideal_time="夜",
        tips=["ツアーは英語対応あり", "コートに匂いが付くので気になる場合はカバーを"],
        booking_required=True,
    ),
    Experience(
        city="那覇",
        title="国際通りサンライズヨガと朝ごはん市場",
        description=(
            "国際通り屋上テラスでサンライズヨガを楽しみ、牧志公設市場で島野菜たっぷりの沖縄そばを味わうヘルシーな朝。"
        ),
        activity_type="リラクゼーション",
        budget="¥",
        weather="晴れ",
        mood="リフレッシュ",
        duration_hours=3,
        highlights=["テラスヨガ", "牧志公設市場", "島野菜そば"],
        ideal_season="春",
        ideal_time="早朝",
        tips=["ヨガマットは貸出あり", "市場は現金決済が中心"],
    ),
    Experience(
        city="那覇",
        title="瀬長島ウミカジテラスサンセットと足湯",
        description=(
            "瀬長島ウミカジテラスで夕景を眺めながらショッピングを楽しみ、島の足湯スポットで飛行機を眺めつつリラックスする海辺の黄昏タイム。"
        ),
        activity_type="アウトドア",
        budget="¥",
        weather="晴れ",
        mood="ロマンチック",
        duration_hours=3,
        highlights=["ウミカジテラスの夕景", "飛行機の離着陸", "天然温泉足湯"],
        ideal_season="夏",
        ideal_time="夕方",
        tips=["日没時間に合わせて訪問", "足湯用のタオルを持参"],
    ),
    Experience(
        city="那覇",
        title="首里金城町石畳散歩と琉球茶房",
        description=(
            "首里城近くの金城町石畳道を散策し、琉球茶房でさんぴん茶とちんすこうを楽しむ歴史さんぽ。"
        ),
        activity_type="カルチャー",
        budget="¥",
        weather="晴れ",
        mood="ノスタルジック",
        duration_hours=2,
        highlights=["石畳道", "赤瓦の古民家", "琉球茶スイーツ"],
        ideal_season="冬",
        ideal_time="午前",
        tips=["石畳は滑りやすいのでスニーカー推奨", "茶房は席数が少ないためピークを避ける"],
    ),
    Experience(
        city="那覇",
        title="慶良間諸島日帰りシュノーケルツアー",
        description=(
            "那覇から高速船で慶良間諸島へ渡り、ガイド付きシュノーケルでサンゴ礁とウミガメを観察する日帰りマリンアクティビティ。"
        ),
        activity_type="アウトドア",
        budget="¥¥",
        weather="晴れ",
        mood="アクティブ",
        duration_hours=8,
        highlights=["サンゴ礁シュノーケル", "ウミガメとの遭遇", "無人島上陸"],
        ideal_season="夏",
        ideal_time="終日",
        tips=["船酔い対策の薬を準備", "水着の上にラッシュガードを着用"],
        booking_required=True,
    ),
    Experience(
        city="那覇",
        title="糸満漁港朝市と海人食堂",
        description=(
            "糸満漁港の朝市でマグロ解体ショーを見学し、海人食堂で海ブドウ丼とアーサ汁を味わうローカルシーフード体験。"
        ),
        activity_type="グルメ",
        budget="¥",
        weather="晴れ",
        mood="ローカル",
        duration_hours=3,
        highlights=["マグロ解体ショー", "海人食堂", "海ブドウ丼"],
        ideal_season="冬",
        ideal_time="朝",
        tips=["朝市は8時までに到着", "市場は濡れているので滑りにくい靴で"],
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
