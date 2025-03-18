def serialize_product(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "stock": product["stock"],
        "category": product["category"],
    }

def serialize_list(products) -> list:
    return [serialize_product(product) for product in products]
