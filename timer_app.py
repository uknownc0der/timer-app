import streamlit as st
import time

def main():
    st.set_page_config(page_title="Timer App", page_icon="⏳", layout="centered")
    
    # Timer Selection
    st.title("Select a Timer")
    timer_choice = st.radio("Choose a timer:", ["10 minutes", "15 minutes", "20 minutes"], index=0)
    
    timer_map = {"10 minutes": 600, "15 minutes": 900, "20 minutes": 1200}
    selected_time = timer_map[timer_choice]
    
    if st.button("Start Timer"):
        start_timer(selected_time)

def start_timer(duration):
    st.session_state.running = True
    
    timer_display = st.empty()
    
    if st.button("Stop"):
        st.session_state.running = False
    
    while duration > 0 and st.session_state.running:
        minutes, seconds = divmod(duration, 60)
        timer_display.markdown(f"# {minutes:02}:{seconds:02}", unsafe_allow_html=True)
        time.sleep(1)
        duration -= 1
    
    if not st.session_state.running or duration == 0:
        timer_display.markdown("# 🎉 Time's Up!", unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
