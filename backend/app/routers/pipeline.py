from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.pipeline_stage import PipelineStage
from app.models.order import Order
from app.models.client import Client
from app.schemas.pipeline_stage import PipelineStageCreate, PipelineStageRead
from app.schemas.order import OrderRead
from typing import List

router = APIRouter(prefix="/pipeline", tags=["Pipeline"])

@router.post("/stage", response_model=PipelineStageRead)
def create_stage(stage: PipelineStageCreate, db: Session = Depends(get_db)):
    db_stage = PipelineStage(**stage.dict())
    db.add(db_stage)
    db.commit()
    db.refresh(db_stage)
    return db_stage

@router.get("/stages", response_model=List[PipelineStageRead])
def list_stages(db: Session = Depends(get_db)):
    return db.query(PipelineStage).order_by(PipelineStage.order).all()

@router.get("/kanban", response_model=List[dict])
def kanban_view(db: Session = Depends(get_db)):
    stages = db.query(PipelineStage).order_by(PipelineStage.order).all()
    kanban = []
    for stage in stages:
        orders = db.query(Order).filter(Order.pipeline_stage_id == stage.id).all()
        kanban.append({
            "stage": PipelineStageRead.from_orm(stage),
            "orders": [OrderRead.from_orm(order) for order in orders]
        })
    return kanban

@router.patch("/move-order/{order_id}", response_model=OrderRead)
def move_order(order_id: int, stage_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    stage = db.query(PipelineStage).filter(PipelineStage.id == stage_id).first()
    if not stage:
        raise HTTPException(status_code=404, detail="Etapa não encontrada")
    order.pipeline_stage_id = stage_id
    db.commit()
    db.refresh(order)
    return order

@router.get("/search", response_model=List[OrderRead])
def search_orders(
    client_name: str = Query(None),
    status: str = Query(None),
    stage_id: int = Query(None),
    event_date_from: str = Query(None),
    event_date_to: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Order)
    if client_name:
        query = query.join(Order.client).filter(Client.name.ilike(f"%{client_name}%"))
    if status:
        query = query.filter(Order.status == status)
    if stage_id:
        query = query.filter(Order.pipeline_stage_id == stage_id)
    if event_date_from:
        query = query.filter(Order.event_date >= event_date_from)
    if event_date_to:
        query = query.filter(Order.event_date <= event_date_to)
    return query.all()
