from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.shared.models import User, UserBooks, Books
from pydantic import UUID4

from typing import List, Optional

from .schemas import UserCreate, UserUpdate, UserResponse


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[UserResponse]:
        stmt = select(User)
        return self.db.execute(stmt).scalars().all()

    def get_users_books(self, id: UUID4) -> List[UserResponse]:
        stmt = (
            select(UserBooks)
            .where(UserBooks.user_id == id)
            .options(
                selectinload(UserBooks.book)
                .load_only(Books.id, Books.title, Books.author)
            )
        )
        return self.db.execute(stmt).scalars().all()

    def get_by_id(self, id: UUID4) -> Optional[UserResponse]:
        stmt = select(User).where(User.id == id)
        return self.db.execute(stmt).scalars().first()

    def create(self, data: UserCreate) -> User:
        obj = User(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, id: UUID4, data: UserUpdate) -> Optional[UserResponse]:
        obj = self.get_by_id(id)
        if not obj:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(obj, key, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, id: UUID4) -> bool:
        obj = self.get_by_id(id)
        if not obj:
            return None
        self.db.delete(obj)
        self.db.commit()
        return True
