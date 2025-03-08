import requests
from utils.config import WEATHER_API_KEY

def get_weather(location):
    """Fetch current weather data from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return None
    
    weather_info = {
        "location": location,
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "conditions": response["weather"][0]["description"]
    }
    
    return weather_info



def get_forecast(location):
    """Fetch 5-day weather forecast from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != "200":
        return None

    forecast_data = {}
    
    for entry in response["list"]:
        date = entry["dt_txt"].split(" ")[0]  # Extract date only
        
        if date not in forecast_data:
            forecast_data[date] = {
                "temperature": entry["main"]["temp"],
                "humidity": entry["main"]["humidity"],
                "conditions": entry["weather"][0]["description"]
            }

    return forecast_data
