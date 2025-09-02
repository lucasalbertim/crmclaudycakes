from sqlalchemy.orm import Session
from app.models.client import Client
from app.models.order import Order
from datetime import datetime, timedelta
from typing import List

# Clientes sem pedidos nos últimos X meses

def get_inactive_clients(db: Session, months: int = 6) -> List[Client]:
    cutoff = datetime.now() - timedelta(days=months*30)
    subq = db.query(Order.client_id).filter(Order.event_date >= cutoff).distinct()
    return db.query(Client).filter(~Client.id.in_(subq)).all()

# Clientes aniversariantes no mês

def get_birthday_clients(db: Session, month: int = None) -> List[Client]:
    if not month:
        month = datetime.now().month
    return db.query(Client).filter(
        Client.wedding_date != None,
        Client.wedding_date.month == month
    ).all()
