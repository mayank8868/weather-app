import requests
from utils.config import YOUTUBE_API_KEY

def get_weather_videos():
    """Fetch weather-related YouTube videos and return embed URLs."""
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q=weather+forecast&type=video&key={YOUTUBE_API_KEY}"
    
    try:
        response = requests.get(url).json()
        
        # Debugging: Print the API response to check structure
        print("YouTube API Response:", response)

        if "items" not in response:
            print("Error: 'items' key not found in response.")
            return []

        videos = []
        for item in response["items"]:
            if "id" in item and "videoId" in item["id"]:
                video_id = item["id"]["videoId"]
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                videos.append(embed_url)
        
        return videos

    except requests.exceptions.RequestException as e:
        print("Error fetching YouTube videos:", e)
        return []

