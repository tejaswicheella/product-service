from pymongo import MongoClient
import os

#Mongo URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://27017")

#Connect to MONGO DB
client = MongoClient(MONGO_URI)
db = client["ecommerce"]
products_collection = db["products"]