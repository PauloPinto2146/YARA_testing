from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TabData(BaseModel):
    url: str
    title: str | None = None
    active: bool | None = None

@app.post("/check")
def check(data: TabData):

    print("Recebido:", data)

    return {
        "score": 72,
        "risk": "high"
    }