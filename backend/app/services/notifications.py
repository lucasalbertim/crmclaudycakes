from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.models.client import Client
from app.core.database import get_db

# Exemplo de função para buscar entregas próximas e gerar notificações

def get_upcoming_deliveries(db: Session, days_ahead: int = 3):
    now = datetime.now()
    future = now + timedelta(days=days_ahead)
    return db.query(Schedule).filter(
        Schedule.delivery_datetime >= now,
        Schedule.delivery_datetime <= future,
        Schedule.status != "entregue"
    ).all()

# Função para gerar mensagem de lembrete

def generate_reminder_message(schedule: Schedule, client: Client):
    return (
        f"Olá {client.name}, lembramos que sua entrega está agendada para "
        f"{schedule.delivery_datetime.strftime('%d/%m/%Y %H:%M')} no local: {schedule.location}. "
        "Qualquer dúvida, estamos à disposição!"
    )
