from fastapi import FastAPI

from app.routes.fitness_routes import router as fitness_router

app = FastAPI(
    title="AI Fitness & Weather Advisor",
    description="AI-powered fitness recommendations using weather and AQI data",
    version="1.0.0"
)

# Include Routes
app.include_router(fitness_router)


# Home Route
@app.get("/")
def home():

    return {
        "message": "AI Fitness & Weather Advisor API Running"
    }


# Health Check Route
@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }