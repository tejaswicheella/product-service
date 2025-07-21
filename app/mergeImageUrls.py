import os
import pandas as pd

#Set up paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")

PRODUCTS_CSV = os.path.join(DATA_DIR, "products_enriched.csv")
IMAGES_CSV = os.path.join(DATA_DIR, "images.csv")
OUTPUT_CSV = os.path.join(DATA_DIR, "products_final.csv")
OUTPUT_JSON = os.path.join(DATA_DIR, "products_final.json")

#Load data
products_df = pd.read_csv(PRODUCTS_CSV)
images_df = pd.read_csv(IMAGES_CSV)

#Clean filename to get id from image
images_df["id"] = images_df["filename"].str.replace(".jpg", "", regex = False).astype(int)

#Merge on product ID
merged_df = pd.merge(products_df, images_df[["id", "link"]], left_on="id", right_on="id", how="left")

#Rename the column
merged_df = merged_df.rename(columns={"link": "image_url"})

#Save enriched product catalog with image urls

merged_df.to_csv(OUTPUT_CSV, index=False)
merged_df.to_json(OUTPUT_JSON, orient="records", indent=2)

print(f"Merge with image URLs.\nCSV: {OUTPUT_CSV}\nJSON: {OUTPUT_JSON}")