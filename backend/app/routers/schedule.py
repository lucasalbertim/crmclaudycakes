from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.schedule import Schedule
from app.models.client import Client
from app.models.order import Order
from app.schemas.schedule import ScheduleCreate, ScheduleRead
from app.services.notifications import get_upcoming_deliveries, generate_reminder_message
from typing import List
import os

router = APIRouter(prefix="/schedules", tags=["Schedules"])
UPLOAD_DIR = "uploads/projects"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=ScheduleRead)
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == schedule.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    if schedule.order_id:
        order = db.query(Order).filter(Order.id == schedule.order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

@router.get("/client/{client_id}", response_model=List[ScheduleRead])
def list_schedules(client_id: int, db: Session = Depends(get_db)):
    return db.query(Schedule).filter(Schedule.client_id == client_id).all()

@router.post("/upload-photo/{schedule_id}", response_model=ScheduleRead)
def upload_project_photo(schedule_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as buffer:
        buffer.write(file.file.read())
    schedule.project_photo = filepath
    db.commit()
    db.refresh(schedule)
    return schedule

@router.get("/upcoming-reminders", response_model=List[ScheduleRead])
def upcoming_reminders(days_ahead: int = 3, db: Session = Depends(get_db)):
    schedules = get_upcoming_deliveries(db, days_ahead)
    reminders = []
    for schedule in schedules:
        client = db.query(Client).filter(Client.id == schedule.client_id).first()
        msg = generate_reminder_message(schedule, client)
        reminders.append({
            "schedule": ScheduleRead.from_orm(schedule),
            "message": msg
        })
    return reminders
