from fastapi import APIRouter
import requests

from app.core.config import OPENWEATHER_API_KEY
from app.core.fallback import fallback
from app.routes.llm import ask_ai

router = APIRouter()

@router.get("/weather/{city}")
def weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {"message": "City not found"}

    data = response.json()

    weather_data = {
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }

    try:
        advice = ask_ai(weather_data)
    except Exception:
        advice = fallback(weather_data)

    return {
        "weather": weather_data,
        "advice": advice
    }