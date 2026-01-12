# main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "eurondb")  # default if not set

if not MONGO_URI:
    raise Exception("MONGODB_URI is not set! Please check your .env file.")

# -----------------------------
# Connect to MongoDB (Async)
# -----------------------------
client = AsyncIOMotorClient(MONGO_URI, tls=True)
db = client[DB_NAME]
euron_data = db["euron_coll"]

print("MongoDB connection successful!")

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="Euron API",
    version="1.0",
    description="API to insert and retrieve data from MongoDB Atlas"
)

# -----------------------------
# Pydantic Model
# -----------------------------
class EuronData(BaseModel):
    name: str
    phone: int
    city: str
    course: str

# -----------------------------
# Serialize MongoDB ObjectId
# -----------------------------
def serialize_mongo(doc: dict) -> dict:
    """Convert _id to string for JSON response"""
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

# -----------------------------
# API Routes
# -----------------------------
@app.post("/euron/insert_data")
async def insert_euron_data(data: EuronData):
    try:
        result = await euron_data.insert_one(data.model_dump())
        return {"id": str(result.inserted_id), "message": "Data inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_eurondata")
async def get_all_data():
    documents = []
    async for doc in euron_data.find():
        documents.append(serialize_mongo(doc))
    return documents

@app.get("/")
async def root():
    return {"message": "Euron API is running. Use /docs for API documentation."}
