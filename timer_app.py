import streamlit as st
import time

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
    
    st.subheader("⏳ Sand Clock Timer")
    
    if st.button("Stop"):
        st.session_state.running = False
    
    top_layer = []
    bottom_layer = []
    
    for _ in range(duration):
        if not st.session_state.running:
            break
        
        if top_layer:
            bottom_layer.append(top_layer.pop())
        else:
            top_layer = ["⬤" for _ in range(10)]
        
        st.write("Top:", " ".join(top_layer))
        st.write("Bottom:", " ".join(bottom_layer))
        time.sleep(1)
    
    if not st.session_state.running or duration == 0:
        st.success("⏳ Time's Up!")
        st.session_state.log.append(f"Used {duration // 60} minutes at {time.strftime('%H:%M:%S')}")
        
if __name__ == "__main__":
    main()
