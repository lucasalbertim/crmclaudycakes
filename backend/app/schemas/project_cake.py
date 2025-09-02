from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProjectCakeBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    photo: Optional[str] = None
    date: Optional[date] = None
    is_reference: Optional[bool] = False

class ProjectCakeCreate(ProjectCakeBase):
    pass

class ProjectCakeRead(ProjectCakeBase):
    id: int
    class Config:
        orm_mode = True
