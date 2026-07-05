from fastapi import FastAPI
from app.routes.weather import router

app = FastAPI(
    title="Weather Chatbot"
)

app.include_router(router)