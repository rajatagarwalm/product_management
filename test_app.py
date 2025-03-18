from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

def test_create_product():
    product_data = {
        "name": "Test Product",
        "description": "This is a test product",
        "price": 50.0,
        "stock": 10,
        "category": "Electronics"
    }
    response = client.post("/products/create", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
