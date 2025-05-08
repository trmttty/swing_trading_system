import streamlit as st
import pandas as pd
import numpy as np

# ページの設定
st.set_page_config(
    page_title="Streamlitチュートリアル",
    page_icon="📊",
    layout="wide"
)

# タイトル
st.title("Streamlitチュートリアル")
st.markdown("Streamlitの基本的な機能を紹介します。")

# サイドバー
st.sidebar.header("ナビゲーション")
page = st.sidebar.radio(
    "表示するセクションを選択してください",
    ["基本機能", "データ可視化", "インタラクティブ機能"]
)

if page == "基本機能":
    st.header("基本機能")
    
    # テキスト入力
    st.subheader("テキスト入力")
    user_input = st.text_input("あなたの名前を入力してください")
    if user_input:
        st.write(f"こんにちは、{user_input}さん！")
    
    # 数値入力
    st.subheader("数値入力")
    number = st.number_input("1から100までの数字を選んでください", 1, 100, 50)
    st.write(f"選択された数字: {number}")
    
    # セレクトボックス
    st.subheader("セレクトボックス")
    option = st.selectbox(
        "好きな色を選んでください",
        ["赤", "青", "緑", "黄色"]
    )
    st.write(f"選択された色: {option}")

elif page == "データ可視化":
    st.header("データ可視化")
    
    # サンプルデータの作成
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # 折れ線グラフ
    st.subheader("折れ線グラフ")
    st.line_chart(chart_data)
    
    # 棒グラフ
    st.subheader("棒グラフ")
    st.bar_chart(chart_data)
    
    # エリアチャート
    st.subheader("エリアチャート")
    st.area_chart(chart_data)

else:
    st.header("インタラクティブ機能")
    
    # スライダー
    st.subheader("スライダー")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    st.write(f"選択された年齢: {age}")
    
    # チェックボックス
    st.subheader("チェックボックス")
    if st.checkbox("詳細を表示"):
        st.write("これはチェックボックスが選択された時に表示される詳細情報です。")
    
    # ファイルアップロード
    st.subheader("ファイルアップロード")
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("アップロードされたデータ:")
        st.dataframe(data.head()) 