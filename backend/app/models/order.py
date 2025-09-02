from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    contract_number = Column(String(50), nullable=True)
    event_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String(30), nullable=False, default="planejamento")
    total_value = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    pipeline_stage_id = Column(Integer, ForeignKey("pipeline_stages.id"), nullable=True)

    client = relationship("Client", back_populates="orders")
    schedules = relationship("Schedule", back_populates="order")
    transactions = relationship("Transaction", back_populates="order")
    installments = relationship("Installment", back_populates="order")
    pipeline_stage = relationship("PipelineStage")
