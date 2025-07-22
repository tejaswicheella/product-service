import os
import pandas as pd
import random
from faker import Faker

fake = Faker()

#Load original products csv file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
INPUT_CSV = os.path.join(DATA_DIR, "products.csv")
OUTPUT_CSV = os.path.join(DATA_DIR, "products_enriched.csv")

df = pd.read_csv(INPUT_CSV)


# Category-wise descriptions
CATEGORY_DESCRIPTIONS = {
    "Apparel": [
        "Crafted from premium cotton for all-day comfort.",
        "A modern fit made with breathable fabric for stylish wear.",
        "Perfect for everyday use, casual outings, or work-from-home looks."
    ],
    "Accessories": [
        "An elegant piece to elevate your style.",
        "Designed with precision and timeless charm.",
        "A must-have accessory to complete your outfit."
    ],
    "Footwear": [
        "Built for comfort and durability.",
        "Slip-resistant sole with cushioned support.",
        "Ideal for both casual walks and active days."
    ],
    "Personal Care": [
        "Gentle on all skin types and made with natural ingredients.",
        "Refreshing, long-lasting, and dermatologically tested.",
        "Feel fresh and confident all day long."
    ]
}

def get_description(category):
    return random.choice(CATEGORY_DESCRIPTIONS.get(category, [
        "A high-quality product designed to meet your everyday needs."
    ]))

#Generate enrichment columns

df["description"] = df["masterCategory"].apply(get_description)
df["price"] = df.apply(lambda x: round(random.uniform(10,200), 2), axis=1)
df["rating"] = df.apply(lambda x: round(random.uniform(1.0,5.0), 1), axis=1)
df["stock"] = df.apply(lambda x: random.randint(0,100), axis = 1)
df["brand"] = df.apply(lambda x: fake.company(), axis = 1)


df.to_csv(OUTPUT_CSV, index=False)
print("Writing file to:", OUTPUT_CSV)
print("✅ Enriched product data saved to 'products_enriched.csv'")