import pytest
from database.db_operations import insert_weather_data, get_weather_data

def test_insert_weather_data():
    """Test inserting weather data into the database."""
    insert_weather_data("Test City", 25.0, 65, "Clear")
    data = get_weather_data()
    assert len(data) > 0
    assert data[-1]["location"] == "Test City"
