from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    delivery_datetime = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    status = Column(String(30), nullable=False, default="planejamento")
    notes = Column(Text, nullable=True)
    project_photo = Column(String(255), nullable=True)
    latitude = Column(String(30), nullable=True)
    longitude = Column(String(30), nullable=True)

    client = relationship("Client", back_populates="schedules")
    order = relationship("Order", back_populates="schedules")
