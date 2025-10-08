import streamlit as st
from bot import TwitterBot
from scheduler import schedule_posts
from data_loader import load_kaggle_data

st.title("AI Twitter/X Automation Bot")

st.sidebar.header("Bot Settings")
interval_minutes = st.sidebar.number_input("Posting Interval (minutes)", value=30, min_value=5)
active_start = st.sidebar.time_input("Active Start Time", value=None)
active_end = st.sidebar.time_input("Active End Time", value=None)

st.sidebar.subheader("Keywords/Hashtags")
keywords = st.sidebar.text_area("Comma-separated keywords", value="AI,Python,Tech").split(",")

st.sidebar.subheader("Video Feed Integration")
enable_video_feed = st.sidebar.checkbox("Enable FreeSpeech.tube feed", value=True)

if st.button("Start Bot"):
    st.write("Bot is running...")
    # Load dataset
    tweets_df = load_kaggle_data("data/twitter_training.csv")
    # Initialize bot
    bot = TwitterBot(tweets_df)
    # Schedule posting & monitoring
    schedule_posts(bot, interval_minutes, active_start, active_end, keywords, enable_video_feed)
    st.success("Bot started successfully!")
