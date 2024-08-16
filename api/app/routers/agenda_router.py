from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.app import models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Agenda)
def create_agenda(agenda: schemas.AgendaCreate, db: Session = Depends(get_db)):
    db_agenda = models.Agenda(**agenda.dict())
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

@router.get("/{agenda_id}", response_model=schemas.Agenda)
def read_agenda(agenda_id: int, db: Session = Depends(get_db)):
    db_agenda = db.query(models.Agenda).filter(models.Agenda.id_agenda == agenda_id).first()
    if db_agenda is None:
        raise HTTPException(status_code=404, detail="Agenda not found")
    return db_agenda

@router.put("/{agenda_id}", response_model=schemas.Agenda)
def update_agenda(agenda_id: int, agenda: schemas.AgendaCreate, db: Session = Depends(get_db)):
    db_agenda = db.query(models.Agenda).filter(models.Agenda.id_agenda == agenda_id).first()
    if db_agenda is None:
        raise HTTPException(status_code=404, detail="Agenda not found")
    for key, value in agenda.dict().items():
        setattr(db_agenda, key, value)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

@router.delete("/{agenda_id}", response_model=schemas.Agenda)
def delete_agenda(agenda_id: int, db: Session = Depends(get_db)):
    db_agenda = db.query(models.Agenda).filter(models.Agenda.id_agenda == agenda_id).first()
    if db_agenda is None:
        raise HTTPException(status_code=404, detail="Agenda not found")
    db.delete(db_agenda)
    db.commit()
    return db_agenda
