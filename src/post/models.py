import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
