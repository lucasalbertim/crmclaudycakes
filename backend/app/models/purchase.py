from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    date = Column(Date, nullable=False)
    item = Column(String(100), nullable=False)
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="pendente")  # pendente, pago
    notes = Column(Text, nullable=True)

    supplier = relationship("Supplier", back_populates="purchases")
