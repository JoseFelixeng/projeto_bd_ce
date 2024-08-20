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

@router.post("/discente/", response_model=schemas.Discente)
def create_discente(discente: schemas.DiscenteCreate, db: Session = Depends(get_db)):
    db_discente = models.Discente(**discente.dict())
    db.add(db_discente)
    db.commit()
    db.refresh(db_discente)
    return db_discente

@router.get("/{discente_id}", response_model=schemas.Discente)
def read_discente(discente_id: int, db: Session = Depends(get_db)):
    db_discente = db.query(models.Discente).filter(models.Discente.id_discente == discente_id).first()
    if db_discente is None:
        raise HTTPException(status_code=404, detail="Discente not found")
    return db_discente

@router.put("/{discente_id}", response_model=schemas.Discente)
def update_discente(discente_id: int, discente: schemas.DiscenteCreate, db: Session = Depends(get_db)):
    db_discente = db.query(models.Discente).filter(models.Discente.id_discente == discente_id).first()
    if db_discente is None:
        raise HTTPException(status_code=404, detail="Discente not found")
    for key, value in discente.dict().items():
        setattr(db_discente, key, value)
    db.commit()
    db.refresh(db_discente)
    return db_discente

@router.delete("/{discente_id}", response_model=schemas.Discente)
def delete_discente(discente_id: int, db: Session = Depends(get_db)):
    db_discente = db.query(models.Discente).filter(models.Discente.id_discente == discente_id).first()
    if db_discente is None:
        raise HTTPException(status_code=404, detail="Discente not found")
    db.delete(db_discente)
    db.commit()
    return db_discente
