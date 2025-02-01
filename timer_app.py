import streamlit as st
import time
import matplotlib.pyplot as plt

# Initialize session state if it doesn't exist
if "running" not in st.session_state:
    st.session_state.running = False
if "total_time" not in st.session_state:
    st.session_state.total_time = 0
if "daily_stats" not in st.session_state:
    st.session_state.daily_stats = {}

def main():
    st.set_page_config(page_title="Timer App", page_icon="⏳", layout="wide")
    
    # Instagram-style UI
    st.markdown("""
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #fafafa;
                color: #262626;
            }
            .header {
                font-size: 28px;
                font-weight: bold;
                text-align: center;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .timer-box {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 200px;
                font-size: 48px;
                font-weight: bold;
                background-color: #ffffff;
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                margin: auto;
                width: 50%;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .button-container {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-top: 20px;
            }
            .button-container button {
                background-color: #0095f6;
                color: white;
                font-size: 18px;
                border: none;
                padding: 10px 20px;
                border-radius: 30px;
                cursor: pointer;
            }
            .tab-button {
                font-size: 18px;
                color: #0095f6;
                border: none;
                background: none;
                cursor: pointer;
                margin: 0 10px;
            }
            .tab-button:hover {
                text-decoration: underline;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header'>Instagram Style Timer</div>", unsafe_allow_html=True)
    
    # Add tabs for Timer and Stats
    tabs = ["Timer", "Summary", "Daily Stats"]
    tab_selection = st.radio("Select a tab", tabs)
    
    if tab_selection == "Timer":
        show_timer()
    elif tab_selection == "Summary":
        show_summary()
    elif tab_selection == "Daily Stats":
        show_daily_stats()

def show_timer():
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
        
        # Update total time used and daily stats
        st.session_state.total_time += duration
        current_date = time.strftime("%Y-%m-%d")
        if current_date in st.session_state.daily_stats:
            st.session_state.daily_stats[current_date] += duration
        else:
            st.session_state.daily_stats[current_date] = duration

def show_summary():
    # Create a simple line graph showing total time spent
    times = list(st.session_state.daily_stats.values())
    dates = list(st.session_state.daily_stats.keys())
    
    if times:
        plt.figure(figsize=(10, 6))
        plt.plot(dates, times, marker='o', color='b', label='Time spent (seconds)')
        plt.xlabel('Date')
        plt.ylabel('Time spent (seconds)')
        plt.title('Summary of Time Used')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.write("No data available for the summary.")

def show_daily_stats():
    # Show daily stats in a table
    daily_stats_df = list(st.session_state.daily_stats.items())
    
    if daily_stats_df:
        st.write("### Daily Time Usage Stats")
        st.write("Date | Time Used (seconds)")
        for date, time_used in daily_stats_df:
            st.write(f"{date} | {time_used} seconds")
    else:
        st.write("No daily stats available.")

if __name__ == "__main__":
    main()
