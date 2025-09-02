from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.schedule import Schedule
from app.models.order import Order
from app.models.transaction import Transaction
from app.models.pipeline_stage import PipelineStage
from app.models.installment import Installment
from datetime import datetime

def get_dashboard_data(db: Session):
    now = datetime.now()
    # Próximas entregas
    upcoming_deliveries = db.query(Schedule).filter(Schedule.delivery_datetime >= now).order_by(Schedule.delivery_datetime).limit(5).all()
    # Pedidos em produção
    production_orders = db.query(Order).filter(Order.status == "produção").all()
    # Receita prevista no mês
    month = now.month
    year = now.year
    receita_prevista = db.query(func.sum(Transaction.value)).filter(
        Transaction.type == "entrada",
        func.extract('month', Transaction.date) == month,
        func.extract('year', Transaction.date) == year
    ).scalar() or 0
    # Pedidos pendentes de pagamento
    pendentes = db.query(Installment).filter(Installment.status == "em aberto").all()
    # Leads no funil
    pipeline = {}
    stages = db.query(PipelineStage).order_by(PipelineStage.order).all()
    for stage in stages:
        count = db.query(Order).filter(Order.pipeline_stage_id == stage.id).count()
        pipeline[stage.name] = count
    # Alertas automáticos (exemplo: sobrecarga de pedidos)
    alertas = []
    if len(production_orders) > 10:
        alertas.append("Atenção: muitos pedidos em produção!")
    return {
        "upcoming_deliveries": upcoming_deliveries,
        "production_orders": production_orders,
        "receita_prevista": receita_prevista,
        "pendentes_pagamento": pendentes,
        "pipeline": pipeline,
        "alertas": alertas
    }
