from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Metodo Agregação 
@router.get("/usuarios/contagem/")
def get_user_counts(db: Session = Depends(get_db)):
    counts = {}

    counts['docentes'] = db.query(func.count(models.Docente.id_docente)).scalar()
    counts['tecnicos'] = db.query(func.count(models.Tecnico.id_tecnico)).scalar()
    counts['discentes'] = db.query(func.count(models.Discente.id_discente)).scalar()
    counts['administrativos'] = db.query(func.count(models.Administrativo.id_adm)).scalar()

    return counts
