import streamlit as st
import time

# Initialize session state variables if they don't exist
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "is_break" not in st.session_state:
    st.session_state.is_break = False
if "time_left" not in st.session_state:
    st.session_state.time_left = 1500  # Default to 25 minutes (1500 seconds)
if "time_spent" not in st.session_state:
    st.session_state.time_spent = 0  # Total work time in seconds
if "break_time" not in st.session_state:
    st.session_state.break_time = 0  # Total break time in seconds
if "work_sessions" not in st.session_state:
    st.session_state.work_sessions = 0  # Counter for work sessions

# Set up the page layout
st.set_page_config(page_title="Pomodoro Timer", page_icon="⏳", layout="centered")

# Custom CSS for the Pomodoro timer styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            max-width: 400px;
            padding: 20px;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .time-box {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 30px;
            border: 10px solid #ff6347;
            padding: 30px;
            border-radius: 50%;
            width: 200px;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ff6347;
        }
        .button-container {
            display: flex;
            justify-content: space-around;
            gap: 20px;
        }
        .button-container button {
            background-color: #ff6347;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 30px;
            font-size: 18px;
            cursor: pointer;
        }
        .button-container button:hover {
            background-color: #ff4500;
        }
    </style>
""", unsafe_allow_html=True)

# Display header
st.markdown("<div class='title'>Pomodoro Timer</div>", unsafe_allow_html=True)

# Time left display
def format_time(seconds):
    """Format seconds into mm:ss format."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

# Function to start or continue the timer
def start_timer():
    """Start or continue the timer, depending on whether it's a work session or break."""
    while st.session_state.time_left > 0 and st.session_state.is_running:
        minutes_left, seconds_left = divmod(st.session_state.time_left, 60)
        
        # Update the session state time
        st.session_state.time_left -= 1

        # Update the timer display on the page
        timer_display.markdown(f"<div class='time-box'>{format_time(st.session_state.time_left)}</div>", unsafe_allow_html=True)
        
        # Wait for 1 second before updating the timer again
        time.sleep(1)

    # When the timer ends
    if st.session_state.time_left == 0:
        if st.session_state.is_break:
            st.session_state.break_time += 5 * 60  # 5 minutes break
            st.session_state.is_break = False
            st.session_state.time_left = work_duration * 60  # Reset to selected work duration
            st.session_state.work_sessions += 1
            st.success("Break's over! Time to work!")
        else:
            st.session_state.time_spent += work_duration * 60  # Add work session time
            st.session_state.is_break = True
            st.session_state.time_left = 5 * 60  # 5-minute break time
            st.success("Time's up! Take a break!")

# Timer display placeholder
timer_display = st.empty()

# Timer duration selection
work_duration = st.selectbox("Select Work Duration:", [10, 15, 20, 25], index=3)

# Display the timer and buttons
with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        if not st.session_state.is_running:
            if st.button("Start Timer"):
                st.session_state.is_running = True
                st.session_state.time_left = work_duration * 60  # Set to selected work duration
                start_timer()
        else:
            if st.button("Pause Timer"):
                st.session_state.is_running = False

    with col2:
        if st.session_state.is_running and st.button("Reset Timer"):
            st.session_state.is_running = False
            st.session_state.time_left = work_duration * 60  # Reset to selected work duration
            st.session_state.is_break = False
            st.session_state.work_sessions = 0
            st.session_state.time_spent = 0
            st.session_state.break_time = 0

# Display summary stats
st.markdown(f"### Total Work Sessions: {st.session_state.work_sessions}")
st.markdown(f"### Total Work Time: {format_time(st.session_state.time_spent)}")
st.markdown(f"### Total Break Time: {format_time(st.session_state.break_time)}")
