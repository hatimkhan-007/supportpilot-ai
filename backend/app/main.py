
from fastapi import FastAPI

app = FastAPI(
    title="SupportPilot AI",
    description="Intelligent Customer Support Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SupportPilot AI!",
        "status": "Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
