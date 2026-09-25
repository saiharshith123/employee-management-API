# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers.employees import router as employee_router

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Employee Management API",
    description="FastAPI CRUD API with PostgreSQL and SQLAlchemy",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    employee_router
)


@app.get("/")
def root():
    return {
        "message": "Employee Management API is running",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }