def calculate_risk(temp, pm25):

    if temp > 38 or pm25 > 150:
        return "High"

    elif temp > 32 or pm25 > 80:
        return "Moderate"

    return "Low"


def hydration_advice(temp):

    if temp > 35:
        return "Drink 3-4L water today."

    elif temp > 28:
        return "Drink 2.5-3L water today."

    return "Drink around 2L water today."


def best_workout_time(temp, humidity, pm25, activity):

    activity = activity.lower()

    # ---------------------------------
    # Extreme Pollution
    # ---------------------------------
    if pm25 > 120:
        return (
            "Indoor workout recommended today "
            "due to poor air quality."
        )

    # ---------------------------------
    # Very Hot Weather
    # ---------------------------------
    if temp >= 38:

        if activity == "cycling":
            return "5:30 AM - 7:00 AM"

        elif activity == "running":
            return "5:00 AM - 6:30 AM"

        elif activity == "walking":
            return "6:00 AM - 7:00 AM"

        return "Indoor gym workouts preferred."

    # ---------------------------------
    # Hot + Humid Conditions
    # ---------------------------------
    if temp >= 32 or humidity >= 80:

        if activity == "cycling":
            return (
                "6:00 AM - 7:30 AM "
                "or 6:00 PM - 7:00 PM"
            )

        elif activity == "running":
            return (
                "5:30 AM - 7:00 AM "
                "or 6:30 PM - 7:30 PM"
            )

        elif activity == "walking":
            return (
                "6:00 AM - 8:00 AM "
                "or 6:00 PM - 7:30 PM"
            )

        return "Indoor gym workouts recommended."

    # ---------------------------------
    # Pleasant Weather
    # ---------------------------------
    if temp >= 22:

        if activity == "cycling":
            return (
                "6:00 AM - 9:00 AM "
                "or 5:00 PM - 7:00 PM"
            )

        elif activity == "running":
            return (
                "6:00 AM - 8:00 AM "
                "or 5:30 PM - 7:00 PM"
            )

        elif activity == "walking":
            return (
                "6:00 AM - 10:00 AM "
                "or 5:00 PM - 8:00 PM"
            )

        return "Flexible throughout the day."

    # ---------------------------------
    # Cold Weather
    # ---------------------------------
    return "8:00 AM - 11:00 AM"


def outdoor_status(pm25):

    if pm25 > 150:
        return "Unsafe"

    elif pm25 > 80:
        return "Moderate"

    return "Safe"


def activity_advice(activity, temp, pm25):

    activity = activity.lower()

    if activity == "cycling":

        if temp > 35:
            return (
                "Avoid afternoon cycling due to heat."
            )

        if pm25 > 100:
            return (
                "Air quality is poor for "
                "long cycling sessions."
            )

        return "Good conditions for cycling."

    elif activity == "running":

        if temp > 34:
            return (
                "Run during early morning hours."
            )

        return "Weather is suitable for running."

    elif activity == "walking":

        return "Light walking is safe today."

    elif activity == "gym":

        return (
            "Indoor gym workouts are ideal today."
        )

    return "Stay active and hydrated."