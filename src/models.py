from sqlalchemy import (
    Column, String, Text, Boolean, Integer, ForeignKey, TIMESTAMP, Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.database import Base
import uuid
import enum
from datetime import datetime

# Enum for task importance
class ImportanceEnum(str, enum.Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.utcnow)

    items = relationship("Item", secondary="users_items", back_populates="users")

class Item(Base):
    __tablename__ = "items"

    item_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(Text, nullable=True)
    importance = Column(Enum(ImportanceEnum), default=ImportanceEnum.low)
    is_done = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=False), server_default="now()")
    modified_at = Column(TIMESTAMP(timezone=False), onupdate="now()")
    deadline = Column(TIMESTAMP(timezone=False), nullable=True)
    last_updated_by = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))

    users = relationship("User", secondary="users_items", back_populates="items")

class UsersItems(Base):
    __tablename__ = "users_items"

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.item_id", ondelete="CASCADE"), primary_key=True)
