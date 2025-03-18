from fastapi import FastAPI, Request
from app.routes import product_routes
from fastapi.responses import JSONResponse

app = FastAPI(title="Product API", version="1.0.0")

app.include_router(product_routes.router, prefix="/products", tags=["Products"])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "details": str(exc)}
    )
    
@app.get("/", tags=["Health"])
async def health_check():
    return {"message": "API is running"}
