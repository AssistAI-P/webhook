# main.py
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

VERIFY_TOKEN = "assistai123"  # This is your secret token

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return {"status": "failed"}

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Incoming:", data)
    return {"status": "received"}
