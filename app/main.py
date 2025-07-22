from fastapi import FastAPI
from app.routes import router as product_router

app = FastAPI()
app.include_router(product_router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Product API is running"}