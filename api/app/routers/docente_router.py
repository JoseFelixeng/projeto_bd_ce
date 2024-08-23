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

@router.post("/docente/", response_model=schemas.Docente)
def create_docente(docente: schemas.DocenteCreate, db: Session = Depends(get_db)):
    db_docente = models.Docente(**docente.dict())
    db.add(db_docente)
    db.commit()
    db.refresh(db_docente)
    return db_docente

@router.get("/docente/{docente_id}", response_model=schemas.Docente)
def read_docente(docente_id: int, db: Session = Depends(get_db)):
    db_docente = db.query(models.Docente).filter(models.Docente.id_docente == docente_id).first()
    if db_docente is None:
        raise HTTPException(status_code=404, detail="Docente not found")
    return db_docente

@router.put("/docente/{docente_id}", response_model=schemas.Docente)
def update_docente(docente_id: int, docente: schemas.DocenteCreate, db: Session = Depends(get_db)):
    db_docente = db.query(models.Docente).filter(models.Docente.id_docente == docente_id).first()
    if db_docente is None:
        raise HTTPException(status_code=404, detail="Docente not found")
    for key, value in docente.dict().items():
        setattr(db_docente, key, value)
    db.commit()
    db.refresh(db_docente)
    return db_docente

@router.delete("/docente/{docente_id}", response_model=schemas.Docente)
def delete_docente(docente_id: int, db: Session = Depends(get_db)):
    db_docente = db.query(models.Docente).filter(models.Docente.id_docente == docente_id).first()
    if db_docente is None:
        raise HTTPException(status_code=404, detail="Docente not found")
    db.delete(db_docente)
    db.commit()
    return db_docente
