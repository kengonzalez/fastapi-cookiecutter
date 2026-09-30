from datetime import datetime

from enum import Enum
from uuid import uuid4
from sqlalchemy import UUID, DateTime, Integer, String, func, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=text("gen_random_uuid()"))
    email: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )    
