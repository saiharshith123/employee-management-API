# Employee Management API

A FastAPI-based CRUD application for managing employee records using PostgreSQL, SQLAlchemy ORM, Pydantic validation, Swagger documentation, and Postman API testing.

## 🚀 Features

- Create employee records
- View all employees
- View employee by ID
- Update employee details
- Delete employee records
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request validation
- Email validation
- Salary validation
- Duplicate email validation
- RESTful API architecture
- Swagger/OpenAPI documentation
- ReDoc documentation
- Error handling
- Pagination support
- Pytest testing

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| Psycopg2 | PostgreSQL connectivity |
| Uvicorn | ASGI server |
| Swagger/OpenAPI | API documentation |
| Postman | API testing |
| Pytest | Testing |
| Git | Version control |
| GitHub | Project hosting |

## 📁 Project Structure

```text
fastapi_employee_crud/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   └── routers/
│       ├── __init__.py
│       └── employees.py
│
├── tests/
│   └── test_employees.py
│
├── .env
├── requirements.txt
└── README.md
