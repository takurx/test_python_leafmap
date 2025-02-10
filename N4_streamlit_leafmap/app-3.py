import streamlit as st
import datetime
import time

st.title("現在時刻を表示")

# 時刻表示のためのプレースホルダーを作成
placeholder = st.empty()

while True:
    # 現在時刻を取得
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # プレースホルダーを更新
    placeholder.write(f"現在の時刻: {now}")
    
    # 1秒待機
    time.sleep(1)

