from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Installment(Base):
    __tablename__ = "installments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    transaction_id = Column(Integer, ForeignKey("transactions.id"), nullable=True)
    due_date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="em aberto")  # em aberto, pago, atrasado
    paid_date = Column(DateTime, nullable=True)

    order = relationship("Order", back_populates="installments")
    transaction = relationship("Transaction")
