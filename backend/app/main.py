from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SupportPilot AI",
    description="Intelligent Customer Support Platform",
    version="1.0.0"
)

# Allow the React frontend to communicate
# with the FastAPI backend.

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SupportPilot AI!",
        "status": "Backend is running"
    }

@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "application": "SupportPilot AI",
        "backend": "FastAPI"
    }
