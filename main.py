# main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load env only for local development
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "eurondb")

if not MONGO_URI:
    raise RuntimeError("MONGODB_URI is not set")

# MongoDB client (Atlas handles TLS automatically)
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
euron_data = db["euron_coll"]

app = FastAPI(
    title="Euron API",
    version="1.0"
)

class EuronData(BaseModel):
    name: str
    phone: int
    city: str
    course: str

def serialize_mongo(doc: dict) -> dict:
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

@app.post("/euron/insert_data")
async def insert_euron_data(data: EuronData):
    try:
        result = await euron_data.insert_one(data.model_dump())
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_eurondata")
async def get_all_data():
    try:
        documents = []
        async for doc in euron_data.find():
            documents.append(serialize_mongo(doc))
        return documents
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"status": "API running"}
