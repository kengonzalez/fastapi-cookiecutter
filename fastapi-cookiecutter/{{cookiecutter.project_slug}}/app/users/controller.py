from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from pydantic import UUID4

from app.database import get_db
from .schemas import UserResponse, UserCreate, UserUpdate
from .repository import UserRepository

router = APIRouter(prefix="/users", tags=["/users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = UserRepository(db)
    return users.get_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_user_by_id(id: UUID4, db: Session = Depends(get_db)):
    users = UserRepository(db)
    return users.get_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_new_user(data: UserCreate, db: Session = Depends(get_db)):
    users = UserRepository(db)
    return users.create(data)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponse)
def update_user(id: UUID4, data: UserUpdate, db: Session = Depends(get_db)):
    users = UserRepository(db)
    return users.update(id, data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: UUID4, db: Session = Depends(get_db)):
    users = UserRepository(db)
    return users.delete(id)
