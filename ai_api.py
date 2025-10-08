import requests
import os

AI_API_URL = os.getenv("CUSTOM_AI_API_URL")
API_KEY = os.getenv("CUSTOM_AI_API_KEY")

def generate_tweet(prompt: str) -> str:
    response = requests.post(
        AI_API_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"prompt": prompt, "max_length": 280}
    )
    return response.json().get("generated_text", "Hello World!")

def analyze_sentiment(text: str) -> str:
    response = requests.post(
        AI_API_URL + "/sentiment",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"text": text}
    )
    return response.json().get("sentiment", "Neutral")
