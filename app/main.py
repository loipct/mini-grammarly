from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Grammar Correction API",
    description="An API to check and correct grammar and spelling errors",
    version="1.0.0",
)

app.include_router(api_router)
