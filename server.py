from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os, requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
def chat(data: dict):
    prompt = data.get("prompt", "")
    r = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json"
        },
        json={"model": "gpt-4.1-mini", "input": prompt}
    )
    j = r.json()
    out = j.get("output", [{}])[0].get("content", "")
    return {"output": out}
