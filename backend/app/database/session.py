
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.engine import URL

# Backend directory
BACKEND_DIR = Path(__file__).resolve().parents[2]

# Database storage directory
DATABASE_DIR = BACKEND_DIR / "data"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

# SQLite database file
DATABASE_PATH = DATABASE_DIR / "supportpilot.db"

# Database connection URL
DATABASE_URL = URL.create(
    drivername="sqlite",
    database=str(DATABASE_PATH),
)

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for database models
class Base(DeclarativeBase):
    pass


# Dependency for database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
