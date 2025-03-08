import pytest
from weather.weather_api import get_weather

def test_get_weather_valid():
    """Test fetching weather for a valid location."""
    weather = get_weather("New York")
    assert weather is not None
    assert "temperature" in weather
    assert "humidity" in weather
    assert "conditions" in weather

