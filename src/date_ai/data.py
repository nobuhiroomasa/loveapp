"""Curated experiences database for the Date & Outing AI."""

from __future__ import annotations

from dataclasses import dataclass, field
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
    ideal_season: str = "オールシーズン"
    ideal_time: str = "終日"
    tips: List[str] = field(default_factory=list)
    booking_required: bool = False


BUDGET_LEVELS: Iterable[str] = (
    "¥",
    "¥¥",
    "¥¥¥",
    "¥¥¥¥",
    "¥プレミアム",
)


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
        ideal_season="春〜秋",
        ideal_time="夕方〜夜",
        tips=["レジャーシートと軽食は浅草で調達", "夜風が冷えるので薄手のブランケットを持参"],
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
