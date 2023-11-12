import json
from typing import List
from fastapi import FastAPI, Request
from db.database import DataB, Certificate
from functions.func import Fire, Human
from functions.block import Blockchain


Certificates, database = DataB().stuff()
app = FastAPI()

Fire, Human = Fire(), Human()
blockchain = Blockchain()


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
    query = Certificates.select().order_by(Certificates.c.id.asc())
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


@app.get("/mine_block/{data}/{user}/{workT}/{run}")
def mine_block(data, user, workT, run):
    # get the data we need to create a block
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.create_blockchain(proof, previous_hash, data, user, workT, run)
    response = {
        "message": "Block mined!",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "Username": block["Username"],
        "type": block["type"],
        "data": block["data"],
        "workTime": block["workTime"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    blockchain.mine_blocks()
    return json.dumps(response)


@app.get("/get_chain")
def get_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return json.dumps(response)


@app.get("/find_user/{usrname}")
def get_user(usrname):
    response = []
    for data in blockchain.chain:
        if data["Username"] == usrname:
            response.append(data)
    return json.dumps(response)


@app.get("/find_type/{type2}")
def get_type(type2):
    response = []
    for data in blockchain.chain:
        if data["type"] == type2:
            response.append(data)
    return json.dumps(response)


@app.get("/validate")
def validate():
    return blockchain.is_chain_valid(blockchain.chain)
