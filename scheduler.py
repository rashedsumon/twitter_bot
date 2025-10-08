import schedule
import time
import threading
from datetime import datetime

def schedule_posts(bot, interval_minutes, start_time, end_time, keywords, enable_video_feed):
    def job():
        now = datetime.now().time()
        if start_time <= now <= end_time:
            bot.post_tweet("AI Generated Tweet: " + "Hello World!")  # Placeholder
            bot.engage_with_keywords(keywords)
            if enable_video_feed:
                bot.post_video_content()
    
    schedule.every(interval_minutes).minutes.do(job)
    
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(5)
    
    thread = threading.Thread(target=run_scheduler)
    thread.start()
