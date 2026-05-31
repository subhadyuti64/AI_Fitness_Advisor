import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Fitness & Weather Advisor",
    page_icon="🏃",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(
    """
    <style>

    /* =========================================
       MAIN APP
    ========================================= */

    .stApp {
        background-color: #020617;
        color: white;
    }

    h1, h2, h3, h4 {
        color: white;
    }

    /* =========================================
       AI CARD
    ========================================= */

    .ai-box {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 18px;
        color: white;
        font-size: 18px;
        line-height: 1.8;
        border: 1px solid #334155;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }

    /* =========================================
       TAB STYLING
    ========================================= */

    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: #0f172a;
        padding: 12px;
        border-radius: 16px;
        margin-top: 20px;
    }

    .stTabs [data-baseweb="tab"] {

        height: 65px;

        padding-left: 30px;
        padding-right: 30px;

        background-color: #111827;

        border-radius: 14px;

        color: white;

        font-size: 22px;

        font-weight: 700;

        border: 1px solid #334155;

        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {

        background: linear-gradient(
            135deg,
            #2563eb,
            #1d4ed8
        );

        color: white;

        border: 1px solid #3b82f6;

        box-shadow: 0px 4px 20px rgba(37,99,235,0.4);
    }

    /* =========================================
       METRIC CARDS
    ========================================= */

    div[data-testid="metric-container"] {

        background: linear-gradient(
            135deg,
            #111827,
            #0f172a
        );

        border: 1px solid #334155;

        padding: 20px;

        border-radius: 18px;

        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }

    /* =========================================
       SIDEBAR
    ========================================= */

    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# TITLE
# =====================================================
st.title("🏃 AI Fitness & Weather Advisor")

st.write(
    """
    Get AI-powered workout, cycling, hydration,
    and outdoor safety recommendations based
    on weather and AQI conditions.
    """
)

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.header("⚙ User Input")

city = st.sidebar.text_input(
    "Enter City",
    value="Rourkela"
)

activity = st.sidebar.selectbox(
    "Select Activity",
    [
        "cycling",
        "running",
        "walking",
        "gym"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    This AI system analyzes:

    - Weather
    - AQI
    - Temperature
    - Humidity
    - Outdoor Safety

    to generate personalized fitness advice.
    """
)

# =====================================================
# API URL
# =====================================================
API_URL = "https://ai-fitness-advisor.onrender.com/fitness-advice"

# =====================================================
# BUTTON
# =====================================================
if st.sidebar.button("🚀 Get AI Recommendation"):

    payload = {
        "city": city,
        "activity": activity
    }

    try:

        response = requests.post(API_URL, json=payload)

        data = response.json()

        # =====================================================
        # WEATHER DATA
        # =====================================================
        weather = data["weather"]

        temp = weather["temperature"]
        humidity = weather["humidity"]
        wind_speed = weather["wind_speed"]
        condition = weather["condition"]

        pm25 = weather["aqi"]["pm25"]
        pm10 = weather["aqi"]["pm10"]

        risk_level = data["risk_level"]

        # =====================================================
        # RISK BADGE
        # =====================================================
        if risk_level == "Low":
            risk_badge = "🟢 LOW"

        elif risk_level == "Moderate":
            risk_badge = "🟡 MODERATE"

        else:
            risk_badge = "🔴 HIGH"

        # =====================================================
        # TABS
        # =====================================================
        tab1, tab2, tab3 = st.tabs([
            "🏠 Dashboard",
            "🌫 AQI Analytics",
            "🤖 AI Coach"
        ])

        # =====================================================
        # TAB 1 — DASHBOARD
        # =====================================================
        with tab1:

            st.subheader("🌦 Current Environmental Conditions")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "🌡 Temperature",
                    f"{temp}°C"
                )

            with col2:
                st.metric(
                    "💧 Humidity",
                    f"{humidity}%"
                )

            with col3:
                st.metric(
                    "🌬 Wind Speed",
                    f"{wind_speed} kph"
                )

            with col4:
                st.metric(
                    "🌫 PM2.5",
                    round(pm25, 2)
                )

            # =====================================================
            # FITNESS INTELLIGENCE
            # =====================================================
            st.subheader("🏋 Fitness Intelligence")

            col5, col6 = st.columns(2)

            with col5:
                st.metric(
                    "⚠ Risk Level",
                    risk_badge
                )

            with col6:
                st.metric(
                    "🌳 Outdoor Status",
                    data["outdoor_status"]
                )

            # =====================================================
            # WORKOUT TIME
            # =====================================================
            st.markdown("### 🕒 Best Workout Time")

            st.info(data["best_workout_time"])

            # =====================================================
            # ACTIVITY RECOMMENDATION
            # =====================================================
            st.subheader("🚴 Activity Recommendation")

            st.success(data["activity_advice"])

            # =====================================================
            # HYDRATION
            # =====================================================
            st.subheader("💦 Hydration Guidance")

            st.info(data["hydration"])

            # =====================================================
            # WEATHER SUMMARY CARD
            # =====================================================
            st.subheader("☁ Weather Summary")

            weather_emoji = "☀️"

            if "rain" in condition.lower():
                weather_emoji = "🌧"

            elif "cloud" in condition.lower():
                weather_emoji = "☁️"

            elif "clear" in condition.lower():
                weather_emoji = "☀️"

            elif "mist" in condition.lower():
                weather_emoji = "🌫"

            elif "snow" in condition.lower():
                weather_emoji = "❄️"

            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(
                        135deg,
                        #1e293b,
                        #0f172a
                    );
                    padding: 25px;
                    border-radius: 18px;
                    border: 1px solid #334155;
                    color: white;
                    margin-top: 10px;
                    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
                ">

                <h2 style="
                    margin-bottom:10px;
                    color:white;
                ">
                    {weather_emoji} {condition}
                </h2>

                <p style="
                    font-size:18px;
                    color:#cbd5e1;
                ">
                    Current weather in <b>{city}</b>
                </p>

                <hr style="
                    border: 1px solid #334155;
                ">

                <div style="
                    margin-top:20px;
                    padding:18px;
                    background:#0f172a;
                    border-radius:14px;
                    border:1px solid #334155;
                ">

                <p style="
                    font-size:18px;
                    color:#cbd5e1;
                    line-height:1.8;
                    margin:0;
                ">

                The current weather conditions in
                <b>{city}</b> are favorable with
                <b>{condition.lower()}</b> skies.

                Outdoor visibility is good and
                environmental conditions are currently stable.

                </p>

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        # =====================================================
        # TAB 2 — AQI ANALYTICS
        # =====================================================
        with tab2:

            st.subheader("📊 AQI Analysis")

            aqi_df = pd.DataFrame({
                "Pollutant": ["PM2.5", "PM10"],
                "Value": [pm25, pm10]
            })

            fig = px.bar(
                aqi_df,
                x="Pollutant",
                y="Value",
                title="Air Quality Indicators"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # =====================================================
            # AQI INSIGHTS
            # =====================================================
            st.subheader("🌫 AQI Insights")

            if pm25 < 50:

                st.success(
                    """
                    Air quality is good for
                    outdoor activities.
                    """
                )

            elif pm25 < 100:

                st.warning(
                    """
                    Moderate pollution detected.
                    Sensitive individuals should
                    reduce prolonged outdoor workouts.
                    """
                )

            else:

                st.error(
                    """
                    Poor air quality detected.
                    Avoid outdoor exercise.
                    """
                )

        # =====================================================
        # TAB 3 — AI COACH
        # =====================================================
        with tab3:

            st.subheader("🤖 AI Coach Recommendation")

            st.markdown(
                f"""
                <div class="ai-box">
                {data['ai_advice']}
                </div>
                """,
                unsafe_allow_html=True
            )

    except Exception as e:

        st.error(f"Error: {e}")