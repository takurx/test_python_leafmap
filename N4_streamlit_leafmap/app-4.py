import streamlit as st
import datetime
import time
from pysolar.solar import get_altitude, get_azimuth
from astral import LocationInfo
from astral.sun import sun
import pytz

# 設定（任意の場所を設定）
latitude = 35.6895  # 東京の緯度
longitude = 139.6917  # 東京の経度
timezone = "Asia/Tokyo"

st.title("太陽の情報を表示")

# 現在時刻表示用プレースホルダー
placeholder = st.empty()

while True:
    # 現在時刻を取得
    now = datetime.datetime.now(pytz.timezone(timezone))
    
    # 太陽の高度角と方位角を計算
    altitude = get_altitude(latitude, longitude, now)
    azimuth = get_azimuth(latitude, longitude, now)
    
    # 日の出と日没を計算
    location = LocationInfo("Tokyo", "Japan", timezone, latitude, longitude)
    s = sun(location.observer, date=now.date(), tzinfo=pytz.timezone(timezone))
    sunrise = s["sunrise"].strftime("%H:%M:%S")
    sunset = s["sunset"].strftime("%H:%M:%S")
    
    # Streamlitに表示
    placeholder.markdown(f"""
        **現在の時刻:** {now.strftime("%Y-%m-%d %H:%M:%S")}
        
        **太陽の仰角:** {altitude:.2f}°
        
        **太陽の方位角:** {azimuth:.2f}°
        
        **日の出:** {sunrise}
        
        **日没:** {sunset}
    """)
    
    # 1秒待機
    time.sleep(1)

