"""Minimal API entrypoint using FastAPI."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "AI Research Agent API"}


# Run with: uvicorn api.main:app --reload
