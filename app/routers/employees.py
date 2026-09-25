# app/routers/employees.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import crud
from ..database import get_db
from ..schemas import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    existing_employee = crud.get_employee_by_email(
        db,
        employee.email
    )

    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee with this email already exists"
        )

    try:
        return crud.create_employee(
            db,
            employee
        )

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee email already exists"
        )


@router.get(
    "/",
    response_model=List[EmployeeResponse]
)
def get_all_employees(
    skip: int = Query(
        0,
        ge=0
    ),
    limit: int = Query(
        100,
        ge=1,
        le=100
    ),
    db: Session = Depends(get_db)
):
    return crud.get_employees(
        db,
        skip,
        limit
    )


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee(
        db,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return employee


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    existing_employee = crud.get_employee(
        db,
        employee_id
    )

    if not existing_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    if employee.email:
        email_employee = crud.get_employee_by_email(
            db,
            employee.email
        )

        if (
            email_employee
            and email_employee.id != employee_id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already belongs to another employee"
            )

    try:
        updated_employee = crud.update_employee(
            db,
            employee_id,
            employee
        )

        return updated_employee

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee email already exists"
        )


@router.delete(
    "/{employee_id}"
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.delete_employee(
        db,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }