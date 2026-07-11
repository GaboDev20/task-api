from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Tasks Schemas

class TaskCreate(BaseModel):
    title:str
    description:Optional[str] = None

class TaskUpdate(BaseModel):
    title:str
    description:Optional[str] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True


# User Schemas

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True



