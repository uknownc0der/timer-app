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
    
    st.subheader("🕹️ Tetris Timer")
    
    if st.button("Stop"):
        st.session_state.running = False
    
    tetris_grid = []
    
    for sec in range(1, duration + 1):
        if not st.session_state.running:
            break
        
        tetris_grid.append("⬛")  # Representing seconds as blocks
        st.write(" ".join(tetris_grid))
        time.sleep(1)
    
    if not st.session_state.running or duration == 0:
        st.success("🎉 Time's Up!")
        
if __name__ == "__main__":
    main()
