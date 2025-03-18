# FastAPI CRUD Application with MongoDB

This project is a FastAPI-based CRUD (Create, Read, Update, Delete) API using MongoDB as the database. It follows a structured MVC architecture ensuring scalability and adherence to SOLID principles.

## Features

1. Create, Read, Update, Delete products.

2. Filter products dynamically based on category and price range.

3. Pagination support for listing products.

4. Structured MVC architecture for scalability.

5. MongoDB cloud integration.

## Folder Structure

│── /app
│   │── /models       # MongoDB Schemas
│   │   ├── product_model.py
│   │── /controllers  # Business Logic
│   │   ├── product_controller.py
│   │── /routes       # API Endpoints (Views)
│   │   ├── product_routes.py
│   │── /config       # Database Connection
│   │   ├── db.py
│   │── /utils        # Utility Functions
│   │   ├── mongo_helper.py
│   │   ├── pagination.py
│   │   ├── validation.py
│   │── main.py       # Entry point for FastAPI app
│── test_main.py
│── .env              # Environment Variables
│── requirements.txt  # Dependencies
│── README.md         # Documentation

## Setup Instructions

1. Clone the repository

git clone https://github.com/rajatagarwalm/product_management.git
cd product_management

2. Install dependencies

pip install -r requirements.txt

3. Configure environment variables

Create a .env file and add your MongoDB connection string:

MONGO_URI=mongodb+srv://your_username:your_password@cluster.mongodb.net/?retryWrites=true&w=majority
DATABASE_NAME=your_database_name

4. Run the FastAPI server

uvicorn app.main:app --reload

5. Access API documentation

Once the server is running, open:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc

## API Endpoints