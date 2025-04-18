from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from api.models import models, schemas

def create(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        customer_name=order.customer_name,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def read_all(db: Session):
    return db.query(models.Order).all()

def read_one(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order_query = db.query(models.Order).filter(models.Order.id == order_id)
    update_data = order.model_dump(exclude_unset=True)
    db_order_query.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_query.first()

def delete(db: Session, order_id: int):
    db_order_query = db.query(models.Order).filter(models.Order.id == order_id)
    db_order_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
