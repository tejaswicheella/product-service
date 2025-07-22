from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    # name: Optional[str]
    # price: Optional[float]
    gender:Optional[str]
    masterCategory:Optional[str]
    subCategory:Optional[str]
    baseColour:Optional[str]
    season:Optional[str]
    year:Optional[int]
    usage:Optional[str]
    productDisplayName:Optional[str]
    description:Optional[str]
    price:Optional[float]
    rating:Optional[float]
    stock:Optional[int]
    brand:Optional[str]
    image_url:Optional[str]