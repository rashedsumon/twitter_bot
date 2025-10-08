import tweepy
from ai_api import generate_tweet, analyze_sentiment
from video_feed import fetch_videos

class TwitterBot:
    def __init__(self, dataset, api=None):
        self.dataset = dataset
        self.api = api or self.authenticate()
        
    def authenticate(self):
        # Load credentials from environment variables
        import os
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET")
        )
        return tweepy.API(auth)
    
    def post_tweet(self, text):
        self.api.update_status(text)
        print(f"Posted: {text}")
    
    def reply_to_tweet(self, tweet_id, text):
        self.api.update_status(status=text, in_reply_to_status_id=tweet_id)
        print(f"Replied to {tweet_id}: {text}")
    
    def follow_user(self, user_id):
        self.api.create_friendship(user_id=user_id)
        print(f"Followed user {user_id}")
    
    def engage_with_keywords(self, keywords):
        for keyword in keywords:
            for tweet in tweepy.Cursor(self.api.search_tweets, q=keyword, lang="en").items(5):
                sentiment = analyze_sentiment(tweet.text)
                if sentiment == "Positive":
                    self.reply_to_tweet(tweet.id, generate_tweet(tweet.text))
                    self.follow_user(tweet.user.id)
    
    def post_video_content(self):
        videos = fetch_videos()
        for video in videos:
            caption = generate_tweet(video['title'] + " " + video['description'])
            self.post_tweet(caption)
