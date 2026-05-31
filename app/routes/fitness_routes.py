from fastapi import APIRouter

from app.models.request_models import FitnessRequest

from app.services.weather_service import get_current_weather

from app.services.openai_service import generate_fitness_advice

from app.utils.fitness_utils import (
    calculate_risk,
    hydration_advice,
    best_workout_time,
    outdoor_status,
    activity_advice
)

router = APIRouter()


@router.post("/fitness-advice")
def fitness_advice(request: FitnessRequest):

    city = request.city
    activity = request.activity

    # ---------------------------------
    # Fetch Weather + AQI Data
    # ---------------------------------
    weather_data = get_current_weather(city)

    if not weather_data:
        return {
            "error": "City not found"
        }

    # ---------------------------------
    # Extract Weather Metrics
    # ---------------------------------
    temp = weather_data["temperature"]

    humidity = weather_data["humidity"]

    pm25 = weather_data["aqi"]["pm25"]

    # ---------------------------------
    # Rule-Based Intelligence
    # ---------------------------------
    risk = calculate_risk(temp, pm25)

    hydration = hydration_advice(temp)

    workout_time = best_workout_time(
        temp=temp,
        humidity=humidity,
        pm25=pm25,
        activity=activity
    )

    outdoor = outdoor_status(pm25)

    advice = activity_advice(
        activity,
        temp,
        pm25
    )

    # ---------------------------------
    # OpenAI GenAI Recommendation
    # ---------------------------------
    ai_advice = generate_fitness_advice(
        city=city,
        activity=activity,
        weather_data=weather_data,
        risk=risk,
        hydration=hydration,
        outdoor=outdoor,
        workout_time=workout_time
    )

    # ---------------------------------
    # Final API Response
    # ---------------------------------
    return {
        "city": city,

        "activity": activity,

        "weather": weather_data,

        "risk_level": risk,

        "hydration": hydration,

        "best_workout_time": workout_time,

        "outdoor_status": outdoor,

        "activity_advice": advice,

        "ai_advice": ai_advice
    }