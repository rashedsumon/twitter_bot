import requests

FEED_URL = "https://freespeech.tube/api/videos.json"

def fetch_videos():
    response = requests.get(FEED_URL)
    data = response.json()
    videos = []
    for item in data.get("videos", [])[:5]:
        videos.append({
            "title": item.get("title"),
            "description": item.get("description"),
            "link": item.get("url"),
            "thumbnail": item.get("thumbnail")
        })
    return videos
