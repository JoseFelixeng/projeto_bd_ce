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

@router.post("/", response_model=schemas.Tecnico)
def create_tecnico(tecnico: schemas.TecnicoCreate, db: Session = Depends(get_db)):
    db_tecnico = models.Tecnico(**tecnico.dict())
    db.add(db_tecnico)
    db.commit()
    db.refresh(db_tecnico)
    return db_tecnico

@router.get("/{tecnico_id}", response_model=schemas.Tecnico)
def read_tecnico(tecnico_id: int, db: Session = Depends(get_db)):
    db_tecnico = db.query(models.Tecnico).filter(models.Tecnico.id_tecnico == tecnico_id).first()
    if db_tecnico is None:
        raise HTTPException(status_code=404, detail="Tecnico not found")
    return db_tecnico

@router.put("/{tecnico_id}", response_model=schemas.Tecnico)
def update_tecnico(tecnico_id: int, tecnico: schemas.TecnicoCreate, db: Session = Depends(get_db)):
    db_tecnico = db.query(models.Tecnico).filter(models.Tecnico.id_tecnico == tecnico_id).first()
    if db_tecnico is None:
        raise HTTPException(status_code=404, detail="Tecnico not found")
    for key, value in tecnico.dict().items():
        setattr(db_tecnico, key, value)
    db.commit()
    db.refresh(db_tecnico)
    return db_tecnico

@router.delete("/{tecnico_id}", response_model=schemas.Tecnico)
def delete_tecnico(tecnico_id: int, db: Session = Depends(get_db)):
    db_tecnico = db.query(models.Tecnico).filter(models.Tecnico.id_tecnico == tecnico_id).first()
    if db_tecnico is None:
        raise HTTPException(status_code=404, detail="Tecnico not found")
    db.delete(db_tecnico)
    db.commit()
    return db_tecnico
