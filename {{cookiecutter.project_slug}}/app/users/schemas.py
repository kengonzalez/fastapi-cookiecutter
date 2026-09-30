from datetime import datetime
from pydantic import BaseModel, ConfigDict, UUID4
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserBaseList(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID4


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created_at: datetime
    updated_at: datetime
