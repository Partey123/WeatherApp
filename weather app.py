# weather_api.py
import requests

API_KEY = "f28e35b4b1dd7a343451cf49f362660a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    """Fetch raw weather data from OpenWeather API"""
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        return response
    except Exception as e:
        print("⚠️ API connection failed:", e)
        return None
