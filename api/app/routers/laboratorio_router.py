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

@router.post("/", response_model=schemas.Laboratorio)
def create_laboratorio(laboratorio: schemas.LaboratorioCreate, db: Session = Depends(get_db)):
    db_laboratorio = models.Laboratorio(**laboratorio.dict())
    db.add(db_laboratorio)
    db.commit()
    db.refresh(db_laboratorio)
    return db_laboratorio

@router.get("/{laboratorio_id}", response_model=schemas.Laboratorio)
def read_laboratorio(laboratorio_id: int, db: Session = Depends(get_db)):
    db_laboratorio = db.query(models.Laboratorio).filter(models.Laboratorio.id_lab == laboratorio_id).first()
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratorio not found")
    return db_laboratorio

@router.put("/{laboratorio_id}", response_model=schemas.Laboratorio)
def update_laboratorio(laboratorio_id: int, laboratorio: schemas.LaboratorioCreate, db: Session = Depends(get_db)):
    db_laboratorio = db.query(models.Laboratorio).filter(models.Laboratorio.id_lab == laboratorio_id).first()
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratorio not found")
    for key, value in laboratorio.dict().items():
        setattr(db_laboratorio, key, value)
    db.commit()
    db.refresh(db_laboratorio)
    return db_laboratorio

@router.delete("/{laboratorio_id}", response_model=schemas.Laboratorio)
def delete_laboratorio(laboratorio_id: int, db: Session = Depends(get_db)):
    db_laboratorio = db.query(models.Laboratorio).filter(models.Laboratorio.id_lab == laboratorio_id).first()
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratorio not found")
    db.delete(db_laboratorio)
    db.commit()
    return db_laboratorio
