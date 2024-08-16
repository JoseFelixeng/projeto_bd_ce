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

@router.post("/", response_model=schemas.Horarios)
def create_horarios(horarios: schemas.HorariosCreate, db: Session = Depends(get_db)):
    db_horarios = models.Horarios(**horarios.dict())
    db.add(db_horarios)
    db.commit()
    db.refresh(db_horarios)
    return db_horarios

@router.get("/{horarios_id}", response_model=schemas.Horarios)
def read_horarios(horarios_id: int, db: Session = Depends(get_db)):
    db_horarios = db.query(models.Horarios).filter(models.Horarios.id_horarios == horarios_id).first()
    if db_horarios is None:
        raise HTTPException(status_code=404, detail="Horarios not found")
    return db_horarios

@router.put("/{horarios_id}", response_model=schemas.Horarios)
def update_horarios(horarios_id: int, horarios: schemas.HorariosCreate, db: Session = Depends(get_db)):
    db_horarios = db.query(models.Horarios).filter(models.Horarios.id_horarios == horarios_id).first()
    if db_horarios is None:
        raise HTTPException(status_code=404, detail="Horarios not found")
    for key, value in horarios.dict().items():
        setattr(db_horarios, key, value)
    db.commit()
    db.refresh(db_horarios)
    return db_horarios

@router.delete("/{horarios_id}", response_model=schemas.Horarios)
def delete_horarios(horarios_id: int, db: Session = Depends(get_db)):
    db_horarios = db.query(models.Horarios).filter(models.Horarios.id_horarios == horarios_id).first()
    if db_horarios is None:
        raise HTTPException(status_code=404, detail="Horarios not found")
    db.delete(db_horarios)
    db.commit()
    return db_horarios
