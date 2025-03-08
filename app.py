from flask import Flask, render_template, request
from weather.weather_api import get_weather, get_forecast
from database.db_operations import insert_weather_data
from integrations.maps import get_coordinates
from integrations.youtube import get_weather_videos

app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    forecast_data = None
    videos = []
    lat, lon = None, None

    if request.method == "POST":
        location = request.form.get("location")
        weather_data = get_weather(location)
        
        if weather_data:
            insert_weather_data(location, weather_data["temperature"], weather_data["humidity"], weather_data["conditions"])
            lat, lon = get_coordinates(location)
            forecast_data = get_forecast(location)  # Fetch 5-day forecast
            videos = get_weather_videos()

            # Debugging outputs
            print("YouTube Video URLs:", videos)
            print("Forecast Data:", forecast_data)

    return render_template("index.html", weather=weather_data, forecast=forecast_data, lat=lat, lon=lon, videos=videos)

    

if __name__ == "__main__":
    app.run(debug=True)

