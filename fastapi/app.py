import json
from typing import List
from fastapi import FastAPI, Request
from db.database import DataB, Certificate
from functions.func import Fire, Human


Certificates, database = DataB().stuff()
app = FastAPI()

Fire, Human = Fire(), Human()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def hi():
    return {"MadeBy": "BelitK"}


@app.get("/certs", response_model=List[Certificate])
async def read_certs():
    query = Certificates.select().order_by("id")
    return await database.fetch_all(query)


@app.get("/vision")
async def boxes_and_confidence(request: Request):
    """Object detection using YOLO."""
    a = await request.json()
    image = json.loads(a)["b64"]
    threshold = json.loads(a)["threshold"]
    return Fire.get_coor(image, threshold)


@app.get("/human")
async def human_detection(request: Request):
    """Human detection using Hog-SVM."""
    a = await request.json()
    image = json.loads(a)["b64"]
    return Human.get_human(image)
