# Weather Chatbot using FastAPI + LiteLLM

## Overview
This project is a Weather Chatbot built using FastAPI and LiteLLM. It fetches live weather data from the OpenWeatherMap API and provides intelligent suggestions such as whether to carry an umbrella, wear a jacket, or carry a water bottle. If the AI model is unavailable, the chatbot uses a rule-based fallback method.

## Features
- Live weather information
- AI-generated weather suggestions
- Fallback rule-based recommendations
- FastAPI REST API
- Swagger UI documentation

## Technologies Used
- Python
- FastAPI
- LiteLLM
- OpenWeatherMap API
- Requests
- Python-dotenv

## Project Structure

```
weather_chatbot/
│
├── app/
│   ├── core/
│   ├── routes/
│   └── main.py
│
├── tests/
├── .env
├── requirements.txt
└── server.py
```

## Run the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python server.py
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

## Author

Your Name
