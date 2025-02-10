# https://chatgpt.com/canvas/shared/67a99360e1a88191a12069af90439522

import streamlit as st
import leafmap.foliumap as leafmap

def main():
    st.set_page_config(layout="wide")
    
    st.title("Leafmap 地図アプリ")
    
    # 地図オブジェクトの作成
    m = leafmap.Map()
    
    # 初期マーカー
    locations = {
        "東京": [35.6895, 139.6917],
        "大阪": [34.6937, 135.5023],
        "札幌": [43.0621, 141.3544]
    }
    
    for city, coords in locations.items():
        m.add_marker(coords, popup=city)
    
    # 地図を表示
    m.to_streamlit()
    
    # ユーザーが座標を入力してマーカーを追加
    st.sidebar.header("マーカーを追加")
    lat = st.sidebar.number_input("緯度", value=35.0, format="%.6f")
    lon = st.sidebar.number_input("経度", value=139.0, format="%.6f")
    label = st.sidebar.text_input("ラベル", "新しい地点")
    
    if st.sidebar.button("マーカーを追加"):
        m.add_marker([lat, lon], popup=label)
        st.experimental_rerun()
    
if __name__ == "__main__":
    main()

