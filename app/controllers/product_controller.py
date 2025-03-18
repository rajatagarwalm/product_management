from app.config.db import product_collection
from app.utils.mongo_helper import serialize_product, serialize_list
from app.models.product_model import Product, ProductUpdate, MultipleProducts
from bson import ObjectId
from fastapi import HTTPException

async def create_product(product: Product):
    product_dict = product.dict()
    result = await product_collection.insert_one(product_dict)
    new_product = await product_collection.find_one({"_id": result.inserted_id})
    return serialize_product(new_product)

async def create_multiple_products(products_data: MultipleProducts):
    products_list = [product.dict() for product in products_data.products]
    result = await product_collection.insert_many(products_list)
    return {"inserted_ids": [str(id) for id in result.inserted_ids]}


async def get_product(product_id: str):
    product = await product_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return serialize_product(product)
    return None

async def list_products():
    products = await product_collection.find().to_list(100)
    return serialize_list(products)

async def update_product(product_id: str, product_data: ProductUpdate):
    update_data = {k: v for k, v in product_data.dict().items() if v is not None}
    if update_data:
        await product_collection.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})
    return await get_product(product_id)

async def delete_product(product_id: str):
    result = await product_collection.delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count > 0

async def get_products_paginated(page: int, limit: int):
    skip = (page - 1) * limit
    products_cursor = product_collection.find().skip(skip).limit(limit)
    products = await products_cursor.to_list(length=limit)
    
    for product in products:
        product["_id"] = str(product["_id"])
    
    return products

async def get_filtered_products(category: str = None, min_price: int = None, max_price: int = None, sort: str = None):
    query = {}

    if category:
        query["category"] = category

    if min_price is not None:
        if min_price < 0:
            raise HTTPException(status_code=400, detail="min_price cannot be negative")
        query["price"] = {"$gte": min_price}

    if max_price is not None:
        if max_price < 0:
            raise HTTPException(status_code=400, detail="max_price cannot be negative")
        query["price"] = query.get("price", {})
        query["price"]["$lte"] = max_price

    sort_order = 1 if sort == "asc" else -1 if sort == "dsc" else None
    cursor = product_collection.find(query).sort("price", sort_order) if sort_order else product_collection.find(query)

    products = await cursor.to_list(100)
    for product in products:
        product["_id"] = str(product["_id"])

    return products
