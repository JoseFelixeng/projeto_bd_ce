from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/agendamento/", response_model=schemas.Agendamento)
def create_agendamento(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    db_agendamento = models.Agendamento(**agendamento.dict())
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

@router.get("/{agendamento_id}", response_model=schemas.Agendamento)
def read_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    db_agendamento = db.query(models.Agendamento).filter(models.Agendamento.id_reserva == agendamento_id).first()
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento not found")
    return db_agendamento

@router.put("/{agendamento_id}", response_model=schemas.Agendamento)
def update_agendamento(agendamento_id: int, agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    db_agendamento = db.query(models.Agendamento).filter(models.Agendamento.id_reserva == agendamento_id).first()
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento not found")
    for key, value in agendamento.dict().items():
        setattr(db_agendamento, key, value)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

@router.delete("/{agendamento_id}", response_model=schemas.Agendamento)
def delete_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    db_agendamento = db.query(models.Agendamento).filter(models.Agendamento.id_reserva == agendamento_id).first()
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento not found")
    db.delete(db_agendamento)
    db.commit()
    return db_agendamento
