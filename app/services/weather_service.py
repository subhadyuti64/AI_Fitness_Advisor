import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_current_weather(city: str):

    url = (
        f"https://api.weatherapi.com/v1/current.json?"
        f"key={WEATHER_API_KEY}&q={city}&aqi=yes"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    weather_info = {
        "city": city,
        "temperature": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "condition": data["current"]["condition"]["text"],
        "wind_speed": data["current"]["wind_kph"],
        "aqi": {
            "pm25": data["current"]["air_quality"]["pm2_5"],
            "pm10": data["current"]["air_quality"]["pm10"],
            "co": data["current"]["air_quality"]["co"]
        }
    }

    return weather_info