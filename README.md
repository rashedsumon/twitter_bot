# AI Twitter/X Automation Bot

This is a Python-based automation bot for Twitter/X. It uses AI to intelligently post, reply, follow, and monitor hashtags/keywords.  

## Features
- Automatic tweeting at scheduled intervals
- Active hours control
- AI-powered tweet generation & replies
- Keyword/hashtag monitoring and engagement
- Auto-follow accounts
- Video feed integration from FreeSpeech.tube
- Kaggle dataset-based training

## Setup
1. Clone repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Add your Twitter API credentials and AI API info in .env:
   TWITTER_API_KEY=...
   TWITTER_API_SECRET=...
   TWITTER_ACCESS_TOKEN=...
   TWITTER_ACCESS_SECRET=...
   CUSTOM_AI_API_URL=...
   CUSTOM_AI_API_KEY=...
4. Run the app:
   streamlit run app.py
