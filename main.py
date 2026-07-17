from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "API Free Fire online"
    }

@app.get("/player")
def player(uid: str):

    url = f"https://freefireinfo-zy9l.onrender.com/api/v1/player-profile?uid={uid}&server=BR"

    resposta = requests.get(url)

    return {
        "status_api_externa": resposta.status_code,
        "resposta": resposta.text
    }
