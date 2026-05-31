import os

from dotenv import load_dotenv

from openai import OpenAI

# Load environment variables
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_fitness_advice(
    city,
    activity,
    weather_data,
    risk,
    hydration,
    outdoor,
    workout_time
):

    prompt = f"""
    You are an AI Fitness and Weather Advisor.

    Analyze the following environmental and fitness data.

    City: {city}

    Activity: {activity}

    Temperature: {weather_data['temperature']}°C

    Humidity: {weather_data['humidity']}%

    Weather Condition: {weather_data['condition']}

    Wind Speed: {weather_data['wind_speed']} kph

    PM2.5 AQI: {weather_data['aqi']['pm25']}

    PM10 AQI: {weather_data['aqi']['pm10']}

    Risk Level: {risk}

    Hydration Recommendation: {hydration}

    Outdoor Status: {outdoor}

    Best Workout Time: {workout_time}

    Generate:
    - personalized fitness advice
    - weather-aware recommendations
    - hydration guidance
    - outdoor safety tips

    Keep the response concise and practical.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional AI fitness and "
                    "environment advisor."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    return response.choices[0].message.content