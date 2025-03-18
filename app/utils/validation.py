from fastapi import HTTPException
from bson import ObjectId

def validate_object_id(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID format")
