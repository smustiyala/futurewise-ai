from fastapi import FastAPI

# Main application entry point for FutureWise AI.
# Additional routers will be registered here as the project grows.

from app.database import Base
from app.database import engine

from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FutureWise AI API",
    description="AI-powered financial feasibility and goal planning platform.",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "FutureWise AI API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}