from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.businesses import router as businesses_router

from app.api.auth import router as auth_router
from app.database.session import Base, engine
from app import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")

    yield


app = FastAPI(
    title="SupportPilot AI",
    description="Intelligent Customer Support Platform",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth_router)
app.include_router(businesses_router)


# Frontend communication configuration
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
