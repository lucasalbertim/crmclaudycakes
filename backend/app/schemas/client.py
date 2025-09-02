from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ClientBase(BaseModel):
    name: str
    cpf: str
    phone: str
    email: EmailStr
    wedding_date: Optional[date] = None
    wedding_location: Optional[str] = None
    guests: Optional[int] = None
    bride_name: Optional[str] = None
    groom_name: Optional[str] = None
    preferences: Optional[str] = None
    restrictions: Optional[str] = None
    cake_style: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    class Config:
        orm_mode = True
