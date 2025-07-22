import os
import json
from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
db = client["ecommerce"]
collection = db["products"]

#Load the products data from JSON file
#BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#DATA_FILE = os.path.join(BASE_DIR, "data", "products_final.json")

#DATA_FILE = "/data/products_final.json"

DATA_FILE = os.path.join("/data", "products_final.json")


print("Reading from:", DATA_FILE)

#Read the JSON data
with open(DATA_FILE, "r", encoding="utf-8") as f:
    products = json.load(f)

# Optional: clear old data to avoid duplicates (be careful in prod)
#collection.delete_many({})

#Insert products into mongodb
collection.insert_many(products)


#Avoid Inserting products if already exists
if collection.count_documents({}) ==0:
    collection.insert_many(products)
    print(f"Inserted {len(products)} products into MongoDB")
else:
    print("Products already exists. Skipping insert.")
