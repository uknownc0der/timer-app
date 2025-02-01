import streamlit as st
import time

# Set up the page layout and styling
st.set_page_config(page_title="Pomodoro Timer", page_icon="⏳", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: white;
            color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-weight: bold;
            transition: background-color 0.5s ease;
        }
        .container {
            text-align: center;
            max-width: 400px;
            padding: 20px;
            border-radius: 10px;
            background-color: #f4f4f4;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: opacity 0.5s ease;
        }
        .title {
            font-size: 28px;
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
            z-index: 10;
        }
        .input-box {
            margin-bottom: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
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

# Initialize session state variables if they don't exist
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "time_left" not in st.session_state:
    st.session_state.time_left = 0  # Initial time left (0 means no timer running)

# Format time as MM:SS
def format_time(seconds):
    """Format seconds into mm:ss format."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

# Start timer function with page dimming effect
def start_timer():
    """Start or continue the timer based on the current state."""
    while st.session_state.time_left > 0 and st.session_state.is_running:
        # Calculate the remaining time
        st.session_state.time_left -= 1

        # Calculate the opacity based on the time left
        opacity = max(0.1, st.session_state.time_left / 100)  # Dim the page as time approaches 0
        page_style = f"background-color: rgba(255, 255, 255, {opacity});"

        # Update the page background opacity
        st.markdown(f'<style>body {{ {page_style} }}</style>', unsafe_allow_html=True)

        # Update the timer display
        timer_display.markdown(f"<div class='time-box'>{format_time(st.session_state.time_left)}</div>", unsafe_allow_html=True)

        # Wait for 1 second before updating the timer again
        time.sleep(1)

    if st.session_state.time_left == 0 and st.session_state.is_running:
        st.session_state.is_running = False
        st.session_state.time_left = 0  # Reset time
        st.success("Time's up!")

# Input for time setting
time_input = st.text_input("Enter time in minutes:", "25")

# Timer display placeholder
timer_display = st.empty()

# Display input and buttons
with st.container():
    # Input box to set timer duration
    st.markdown("<div class='input-box'>Set Timer Duration (in minutes):</div>", unsafe_allow_html=True)
    time_input = st.text_input("Enter time in minutes:", "25")
    try:
        time_duration = int(time_input) * 60  # Convert minutes to seconds
    except ValueError:
        time_duration = 0

    # Start/Stop button toggle
    if not st.session_state.is_running:
        if st.button("Start Timer"):
            st.session_state.time_left = time_duration  # Set time for the timer
            st.session_state.is_running = True
            start_timer()
    else:
        if st.button("Stop Timer"):
            st.session_state.is_running = False  # Stop the timer

# Additional feature for reset (optional)
if st.button("Reset Timer"):
    st.session_state.is_running = False
    st.session_state.time_left = 0
    timer_display.empty()
