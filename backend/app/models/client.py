from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    wedding_date = Column(Date, nullable=True)
    wedding_location = Column(String(200), nullable=True)
    guests = Column(Integer, nullable=True)
    bride_name = Column(String(100), nullable=True)
    groom_name = Column(String(100), nullable=True)
    preferences = Column(Text, nullable=True)
    restrictions = Column(Text, nullable=True)
    cake_style = Column(String(100), nullable=True)
    attachments = relationship("Attachment", back_populates="client")
    orders = relationship("Order", back_populates="client")
    schedules = relationship("Schedule", back_populates="client")
    # Histórico e anexos serão modelados em tabelas separadas
