import streamlit as st
import time
import numpy as np

def main():
    st.set_page_config(page_title="Timer App", page_icon="⏳", layout="centered")
    
    # Sidebar for log tracking
    st.sidebar.header("Usage Log")
    if "log" not in st.session_state:
        st.session_state.log = []
    
    if st.sidebar.button("Clear Log"):
        st.session_state.log = []
    
    for entry in st.session_state.log:
        st.sidebar.write(entry)
    
    # Timer Selection
    st.title("Select a Timer")
    timer_choice = st.radio("Choose a timer:", ["10 minutes", "15 minutes", "20 minutes"], index=0)
    
    timer_map = {"10 minutes": 600, "15 minutes": 900, "20 minutes": 1200}
    selected_time = timer_map[timer_choice]
    
    if st.button("Start Timer"):
        start_timer(selected_time)

def start_timer(duration):
    st.session_state.running = True
    st.session_state.paused = False
    
    st.subheader("⏳ Sand Clock Timer")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Pause/Resume"):
            st.session_state.paused = not st.session_state.paused
    
    sand_clock = ["🔲" for _ in range(10)]
    
    while duration > 0 and st.session_state.running:
        if st.session_state.paused:
            time.sleep(1)
            continue
        
        sand_clock.insert(0, "⬤")
        if len(sand_clock) > 10:
            sand_clock.pop()
        
        st.write("\n".join(sand_clock))
        time.sleep(1)
        duration -= 1
        
    if duration == 0:
        st.success("⏳ Time's Up!")
        st.session_state.log.append(f"Used {duration // 60} minutes at {time.strftime('%H:%M:%S')}")
        
if __name__ == "__main__":
    main()
