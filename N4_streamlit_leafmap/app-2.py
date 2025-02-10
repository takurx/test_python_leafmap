import streamlit as st
import time

def countdown_timer(seconds):
    placeholder = st.empty()
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_text = f"{mins:02d}:{secs:02d}"
        placeholder.markdown(f"# ⏳ {timer_text}")
        time.sleep(1)
        seconds -= 1
    placeholder.markdown("# ⏰ Time's up!")

st.title("3-Minute Timer")
if st.button("Start Timer"):
    countdown_timer(180)
