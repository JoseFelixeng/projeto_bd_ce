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

@router.post("/gerencia/", response_model=schemas.Gerencia)
def create_gerencia(gerencia: schemas.GerenciaCreate, db: Session = Depends(get_db)):
    db_gerencia = models.Gerencia(**gerencia.dict())
    db.add(db_gerencia)
    db.commit()
    db.refresh(db_gerencia)
    return db_gerencia

@router.get("/gerencia/{gerencia_id}", response_model=schemas.Gerencia)
def read_gerencia(gerencia_id: int, db: Session = Depends(get_db)):
    db_gerencia = db.query(models.Gerencia).filter(models.Gerencia.id_docente == gerencia_id).first()
    if db_gerencia is None:
        raise HTTPException(status_code=404, detail="Gerencia not found")
    return db_gerencia

@router.put("/gerencia/{gerencia_id}", response_model=schemas.Gerencia)
def update_gerencia(gerencia_id: int, gerencia: schemas.GerenciaCreate, db: Session = Depends(get_db)):
    db_gerencia = db.query(models.Gerencia).filter(models.Gerencia.id_docente == gerencia_id).first()
    if db_gerencia is None:
        raise HTTPException(status_code=404, detail="Gerencia not found")
    for key, value in gerencia.dict().items():
        setattr(db_gerencia, key, value)
    db.commit()
    db.refresh(db_gerencia)
    return db_gerencia

@router.delete("/gerencia/{gerencia_id}", response_model=schemas.Gerencia)
def delete_gerencia(gerencia_id: int, db: Session = Depends(get_db)):
    db_gerencia = db.query(models.Gerencia).filter(models.Gerencia.id_docente == gerencia_id).first()
    if db_gerencia is None:
        raise HTTPException(status_code=404, detail="Gerencia not found")
    db.delete(db_gerencia)
    db.commit()
    return db_gerencia
