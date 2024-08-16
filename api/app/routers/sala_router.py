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

@router.post("/sala", response_model=schemas.Salas)
def create_salas(salas: schemas.SalasCreate, db: Session = Depends(get_db)):
    db_salas = models.Salas(**salas.dict())
    db.add(db_salas)
    db.commit()
    db.refresh(db_salas)
    return db_salas

@router.get("/{sala_id}", response_model=schemas.Salas)
def read_salas(sala_id: int, db: Session = Depends(get_db)):
    db_salas = db.query(models.Salas).filter(models.Salas.id_sala == sala_id).first()
    if db_salas is None:
        raise HTTPException(status_code=404, detail="Salas not found")
    return db_salas

@router.put("/{sala_id}", response_model=schemas.Salas)
def update_salas(sala_id: int, salas: schemas.SalasCreate, db: Session = Depends(get_db)):
    db_salas = db.query(models.Salas).filter(models.Salas.id_sala == sala_id).first()
    if db_salas is None:
        raise HTTPException(status_code=404, detail="Salas not found")
    for key, value in salas.dict().items():
        setattr(db_salas, key, value)
    db.commit()
    db.refresh(db_salas)
    return db_salas

@router.delete("/{sala_id}", response_model=schemas.Salas)
def delete_salas(sala_id: int, db: Session = Depends(get_db)):
    db_salas = db.query(models.Salas).filter(models.Salas.id_sala == sala_id).first()
    if db_salas is None:
        raise HTTPException(status_code=404, detail="Salas not found")
    db.delete(db_salas)
    db.commit()
    return db_salas
    