from datetime import datetime
from typing import Optional
from pydantic import BaseModel

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
