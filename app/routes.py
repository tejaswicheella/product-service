from fastapi import APIRouter, HTTPException, Query
from app.models import Product
from .db import products_collection

router = APIRouter()

@router.get("/products", response_model=list[Product])
def get_all_products(skip: int = Query(0, ge=0), limit: int = Query(10, ge = 1)):
    products = list(products_collection.find({}, {'_id': 0}).skip(skip).limit(limit)) #exclude Mongo _id
    return products

@router.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    product = products_collection.find_one({"id": product_id}, {'_id': 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# @router.get("/")
# def list_products():
#     return [
#         Product(id=1, name="Shirt", price=29.99),
#         Product(id=2, name="Sneakers", price=79.99),
#     ]