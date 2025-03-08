import pandas as pd
from database.db_operations import get_weather_data

def export_to_csv():
    """Export weather data to CSV."""
    data = get_weather_data()
    df = pd.DataFrame(data)
    df.to_csv("weather_data.csv", index=False)
