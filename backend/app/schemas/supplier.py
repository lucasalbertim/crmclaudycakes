from pydantic import BaseModel, EmailStr
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    contact: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    notes: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierRead(SupplierBase):
    id: int
    class Config:
        orm_mode = True
