from fastapi import APIRouter, HTTPException, Query
from app.controllers import product_controller
from app.models.product_model import MultipleProducts, Product, ProductUpdate
from typing import List, Optional

router = APIRouter()

@router.post("/create", response_model=dict)
async def create_product_route(product: Product):
    return await product_controller.create_product(product)

@router.post("/create_bulk", response_model=dict)
async def add_multiple_products(products: MultipleProducts):
    try:
        response = await product_controller.create_multiple_products(products)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{product_id}", response_model=dict)
async def get_product_route(product_id: str):
    product = await product_controller.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/list_all/", response_model=List[dict])
async def list_products_route():
    return await product_controller.list_products()

@router.put("/{product_id}", response_model=dict)
async def update_product_route(product_id: str, product: ProductUpdate):
    updated_product = await product_controller.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", response_model=dict)
async def delete_product_route(product_id: str):
    deleted = await product_controller.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

@router.get("/list/paginate")
async def get_paginated_products(
    page: int = Query(1, alias="page", description="Page number"),
    limit: int = Query(10, alias="limit", description="Items per page")
):
    return await product_controller.get_products_paginated(page, limit)

@router.get("/filter/")
async def filter_products(
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[int] = Query(None, description="Minimum price range"),
    max_price: Optional[int] = Query(None, description="Maximum price range"),
    sort: Optional[str] = Query(None, regex="^(asc|dsc)$", description="Sort by price (asc/dsc)")
):
    """
    Filter products dynamically based on category and price range.
    """
    return await product_controller.get_filtered_products(category, min_price, max_price, sort)

