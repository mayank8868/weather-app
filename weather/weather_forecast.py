import requests
from utils.config import WEATHER_API_KEY

def get_weather_forecast(location):
    """Fetch 5-day weather forecast."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    
    forecast = []
    for entry in response["list"]:
        forecast.append({
            "date": entry["dt_txt"],
            "temp": entry["main"]["temp"],
            "conditions": entry["weather"][0]["description"]
        })
    
    return forecast
