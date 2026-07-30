import os
import streamlit as st

# --- ページ基本設定 ---
st.set_page_config(
    page_title="思考スキル＆ツール活用ナビ",
    page_icon="🧩",
    layout="wide"
)

st.title("🧩 思考スキル＆ツール活用ナビ")
st.write("児童・生徒に行わせたい「思考の働き」や「思考スキル」から、最適な思考ツール（シンキングツール）とひな型を探せるアプリです。")

# --- 19の思考スキル データベース ---
SKILLS_DATA = [
    {
        "id": 1,
        "skill": "多面的にみる",
        "work": "1つの物事や出来事を複数の視点・立場から捉える",
        "tool": "Yチャート / Xチャート / PMIシート",
        "category": "発想・多角化",
        "filename": "y_chart.pdf"
    },
    {
        "id": 2,
        "skill": "変化をとらえる",
        "work": "時間の経過や状況に伴う移り変わりを捉える",
        "tool": "ステップチャート / 変化（Before/After）シート",
        "category": "プロセス・順序",
        "filename": "step_chart.pdf"
    },
    {
        "id": 3,
        "skill": "順序立てる",
        "work": "時間軸や手順、優先順位に沿って並べる",
        "tool": "フローチャート / シーケンスチャート",
        "category": "プロセス・順序",
        "filename": "flow_chart.pdf"
    },
    {
        "id": 4,
        "skill": "比較する",
        "work": "2つ以上の対象の共通点や相違点を明確にする",
        "tool": "ベン図 / Tチャート",
        "category": "整理・分析",
        "filename": "venn_diagram.pdf"
    },
    {
        "id": 5,
        "skill": "分類する",
        "work": "基準を設けて情報をグループに分ける",
        "tool": "マトリックス / XYチャート（座標軸）",
        "category": "整理・分析",
        "filename": "matrix.pdf"
    },
    {
        "id": 6,
        "skill": "変換する（図、絵など）",
        "work": "言葉の情報を図、絵、表などの形式に置き換える",
        "tool": "イメージマップ / イラスト・図解シート",
        "category": "表現・再構築",
        "filename": "image_map.pdf"
    },
    {
        "id": 7,
        "skill": "関係づける",
        "work": "要素同士の関係（因果関係、対立関係など）をつなぐ",
        "tool": "クラゲチャート / バブルチャート",
        "category": "構造・論理",
        "filename": "jellyfish_chart.pdf"
    },
    {
        "id": 8,
        "skill": "関連づける",
        "work": "提示された情報と、自分の経験・既習事項・身近な出来事を結びつける",
        "tool": "コネクション（連結）シート / KWL表",
        "category": "構造・論理",
        "filename": "kwl_chart.pdf"
    },
    {
        "id": 9,
        "skill": "理由づける",
        "work": "考えや主張に対する根拠や理由を明確にする",
        "tool": "クラゲチャート / 三角ロジック",
        "category": "構造・論理",
        "filename": "triangle_logic.pdf"
    },
    {
        "id": 10,
        "skill": "見通す",
        "work": "この後どうなるか、目的達成までの道筋や結果を予測・計画する",
        "tool": "ピラミッドチャート / フローチャート",
        "category": "プロセス・順序",
        "filename": "pyramid_chart.pdf"
    },
    {
        "id": 11,
        "skill": "抽象化する",
        "work": "個別の具体的な情報から共通する本質やパターン・概念をまとめる",
        "tool": "ピラミッドチャート（下→上） / 概念マップ",
        "category": "整理・分析",
        "filename": "pyramid_up.pdf"
    },
    {
        "id": 12,
        "skill": "焦点化する",
        "work": "多くの情報の中から重要・必要なものに絞り込む",
        "tool": "ダイヤモンドナイン / ピラミッドチャート",
        "category": "評価・選択",
        "filename": "diamond_nine.pdf"
    },
    {
        "id": 13,
        "skill": "評価する",
        "work": "基準をもとに判断・価値づけを行う",
        "tool": "ルーブリック評価表 / PMIシート",
        "category": "評価・選択",
        "filename": "pmi_sheet.pdf"
    },
    {
        "id": 14,
        "skill": "応用する",
        "work": "得た知識や概念を別の新しい状況や課題に当てはめる",
        "tool": "アナロジー（類推）シート / PMIシート",
        "category": "発想・多角化",
        "filename": "analogy_sheet.pdf"
    },
    {
        "id": 15,
        "skill": "構造化する",
        "work": "散らばった情報群全体の関係性や体系を整理してまとめる",
        "tool": "フィッシュボーン（特性要因図） / コンセプトマップ",
        "category": "構造・論理",
        "filename": "fishbone.pdf"
    },
    {
        "id": 16,
        "skill": "推論する",
        "work": "手持ちの事実やデータから、見えない事実や結論を導き出す",
        "tool": "キャンディチャート / ステップチャート",
        "category": "構造・論理",
        "filename": "reasoning_chart.pdf"
    },
    {
        "id": 17,
        "skill": "具体化する",
        "work": "抽象的な概念やルールを、具体的な例や言葉・数値に落とし込む",
        "tool": "ピラミッドチャート（上→下） / バブルチャート",
        "category": "表現・再構築",
        "filename": "pyramid_down.pdf"
    },
    {
        "id": 18,
        "skill": "広げてみる",
        "work": "枠にとらわれず、アイディアや関連する要素を自由に拡散させる",
        "tool": "ウェビング（マインドマップ） / ブレインストーミングシート",
        "category": "発想・多角化",
        "filename": "webbing.pdf"
    },
    {
        "id": 19,
        "skill": "要約する",
        "work": "全体の要点を整理し、短く簡潔にまとめる",
        "tool": "キャンディチャート / まとめシート",
        "category": "表現・再構築",
        "filename": "candy_chart.pdf"
    }
]

# --- ヘルパー関数: ダウンロードボタンの表示 ---
def render_download_button(filename, tool_name):
    # PDFファイルを置くフォルダ名
    file_path = os.path.join("templates", filename)
    
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"📄 {tool_name.split('/')[0].strip()} のひな型(PDF)をダウンロード",
                data=f,
                file_name=filename,
                mime="application/pdf"
            )
    else:
        # PDFファイルが未配置の場合のメッセージ
        st.caption(f"※ ひな型ファイル（`templates/{filename}`）を配置すると、ここから直接ダウンロードできるようになります。")

# --- UIメイン処理 ---
st.divider()

# タブ切り替え
tab1, tab2, tab3 = st.tabs([
    "💡 思考スキルから選ぶ", 
    "🔍 働き・キーワードで検索", 
    "📚 19のスキル一覧表"
])

# 【タブ1】思考スキルから選ぶ
with tab1:
    st.subheader("19の思考スキルから選択")
    
    # スキル名の選択ボックス
    skill_list = [f"{item['id']}. {item['skill']}" for item in SKILLS_DATA]
    selected_skill_str = st.selectbox("行わせたい思考スキルを選んでください:", skill_list)
    
    # 選択されたスキルのIDを取得してデータを抽出
    selected_id = int(selected_skill_str.split(".")[0])
    info = next(item for item in SKILLS_DATA if item["id"] == selected_id)
    
    # カード状の表示
    st.markdown(f"### 思考スキル：**【{info['skill']}】**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**【期待される思考の働き】**\n\n{info['work']}")
    with col2:
        st.success(f"**【対応する思考ツール】**\n\n{info['tool']}")
    
    # ダウンロード機能
    render_download_button(info["filename"], info["tool"])

# 【タブ2】働き・キーワードで検索
with tab2:
    st.subheader("やりたいこと・キーワードから探す")
    keyword = st.text_input("検索ワードを入力（例：「共通点」「アイデア」「因果関係」「理由」など）:")
    
    if keyword:
        # 検索条件（スキル名、働き、ツール名にマッチするか）
        results = [
            item for item in SKILLS_DATA 
            if keyword in item["work"] or keyword in item["skill"] or keyword in item["tool"]
        ]
        
        if results:
            st.write(f"🔍 **{len(results)} 件** のスキルが見つかりました：")
            for res in results:
                with st.expander(f"【{res['skill']}】 - {res['tool']}"):
                    st.write(f"**期待される働き:** {res['work']}")
                    st.write(f"**分類:** {res['category']}")
                    render_download_button(res["filename"], res["tool"])
        else:
            st.warning("該当する思考スキルが見つかりませんでした。別のキーワードで試してください。")

# 【タブ3】19のスキル一覧表
with tab3:
    st.subheader("教科共通の思考スキル 19選 一覧")
    
    # 表形式で全データ表示
    table_data = [
        {
            "No.": item["id"],
            "思考スキル": item["skill"],
            "期待される思考の働き": item["work"],
            "対応する主な思考ツール": item["tool"],
            "カテゴリ": item["category"]
        }
        for item in SKILLS_DATA
    ]
    st.dataframe(table_data, use_container_width=True, hide_index=True)