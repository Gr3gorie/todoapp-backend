from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: Optional[str] = None
    password: str

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    created_at: Optional[str] = None

    class Config:
        orm_mode = True

class NoteBase(BaseModel):
    description: Optional[str] = None
    importance: Optional[str] = None
    is_done: bool = False
    is_deleted: bool = False
    deadline: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    item_id: UUID
    users: List[User] = []

    class Config:
        orm_mode = True
