import streamlit as st
import time

def main():
    st.set_page_config(page_title="Timer App", page_icon="⏳", layout="wide")
    
    # Initialize session state if it doesn't exist
    if "running" not in st.session_state:
        st.session_state.running = False
    
    # Twitter-style UI
    st.markdown("""
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #15202b;
                color: #ffffff;
            }
            .title {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .timer-box {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 200px;
                font-size: 48px;
                font-weight: bold;
                background-color: #192734;
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                margin: auto;
                width: 50%;
            }
            .button-container {
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 20px;
            }
            .button-container button {
                background-color: #1da1f2;
                color: white;
                font-size: 18px;
                border: none;
                padding: 10px 20px;
                border-radius: 25px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='title'>Select a Timer</div>", unsafe_allow_html=True)
    
    timer_choice = st.radio("Choose a timer:", ["10 minutes", "15 minutes", "20 minutes"], index=0)
    
    timer_map = {"10 minutes": 600, "15 minutes": 900, "20 minutes": 1200}
    selected_time = timer_map[timer_choice]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Start Timer", key="start"):
            start_timer(selected_time)
    
    with col2:
        if st.button("Stop Timer", key="stop"):
            st.session_state.running = False

def start_timer(duration):
    st.session_state.running = True
    
    timer_display = st.empty()
    
    while duration > 0 and st.session_state.running:
        minutes, seconds = divmod(duration, 60)
        timer_display.markdown(f"<div class='timer-box'>{minutes:02}:{seconds:02}</div>", unsafe_allow_html=True)
        time.sleep(1)
        duration -= 1
    
    if not st.session_state.running or duration == 0:
        timer_display.markdown("<div class='timer-box'>🎉 Time's Up!</div>", unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
