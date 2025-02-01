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
    
    st.subheader("⏳ Timer Box")
    
    if st.button("Stop"):
        st.session_state.running = False
    
    grid_size = 10  # Box width limit
    box = [["⬜" for _ in range(grid_size)] for _ in range(grid_size)]
    filled_cells = 0
    total_cells = grid_size * grid_size
    
    container = st.empty()
    
    while filled_cells < total_cells and filled_cells < duration and st.session_state.running:
        row = filled_cells // grid_size
        col = filled_cells % grid_size
        box[row][col] = "⬛"
        filled_cells += 1
        
        box_display = "\n".join([" ".join(row) for row in box])
        container.write(f"```{box_display}```")
        time.sleep(1)
    
    if not st.session_state.running or filled_cells >= duration:
        st.success("🎉 Time's Up!")
        
if __name__ == "__main__":
    main()
