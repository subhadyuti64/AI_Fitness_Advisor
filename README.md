# 🌦️ AI Fitness & Weather Advisor

An AI-powered fitness recommendation system that combines **real-time weather conditions**, **air quality data (AQI)**, and **OpenAI-generated insights** to provide personalized workout recommendations and outdoor activity guidance.

---

## 🚀 Live Demo

### Frontend

```text
https://aifitnessadvisor-subhadyuti64.streamlit.app/
```

### Backend API

```text
https://ai-fitness-advisor.onrender.com
```

---

## 📌 Features

### 🌤 Real-Time Weather Analysis

* Current temperature
* Humidity
* Weather conditions
* Wind speed

### 🌫 Air Quality Monitoring

* PM2.5 levels
* PM10 levels
* Carbon monoxide (CO) levels

### 🏃 Fitness Recommendations

* Running
* Walking
* Cycling
* Outdoor workouts
* General fitness activities

### 🤖 AI-Powered Advice

Uses OpenAI GPT to generate:

* Personalized fitness suggestions
* Outdoor safety recommendations
* Hydration guidance
* Weather-aware workout plans

### 📊 Interactive Dashboard

* Weather metrics
* AQI visualization
* Risk assessment
* Workout recommendations

---

## 🛠 Tech Stack

### Frontend

* Streamlit
* Plotly

### Backend

* FastAPI
* Python

### AI

* OpenAI GPT-4.1 Mini

### APIs

* WeatherAPI

### Data Processing

* Pandas
* Requests

---

## 📂 Project Structure

```text
AI_Fitness_Advisor/
│
├── app/
│   ├── models/
│   │   └── request_models.py
│   │
│   ├── routes/
│   │   └── fitness_routes.py
│   │
│   ├── services/
│   │   ├── weather_service.py
│   │   └── openai_service.py
│   │
│   ├── utils/
│   │   └── fitness_utils.py
│   │
│   └── main.py
│
├── frontend.py
│
├── requirements.txt
│
├── .env
│
└── README.md
```
## Author - Subhadyuti Rath
