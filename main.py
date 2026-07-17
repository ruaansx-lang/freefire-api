from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status":"API Free Fire online"}

@app.get("/player")
def player(uid: str):

    url = f"https://free-ff-api-src-5plp.onrender.com/api/v1/account?region=BR&uid={uid}"

    resposta = requests.get(url)

    return resposta.json()
