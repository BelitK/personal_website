from typing import List
from fastapi import FastAPI
from db.database import DataB, Certificate


Certificates, database = DataB().stuff()
app = FastAPI()


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
