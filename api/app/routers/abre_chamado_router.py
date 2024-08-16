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

@router.post("/", response_model=schemas.Abre_chamado)
def create_abre_chamado(abre_chamado: schemas.Abre_chamadoCreate, db: Session = Depends(get_db)):
    db_abre_chamado = models.Abre_chamado(**abre_chamado.dict())
    db.add(db_abre_chamado)
    db.commit()
    db.refresh(db_abre_chamado)
    return db_abre_chamado

@router.get("/{abre_chamado_id}", response_model=schemas.Abre_chamado)
def read_abre_chamado(abre_chamado_id: int, db: Session = Depends(get_db)):
    db_abre_chamado = db.query(models.Abre_chamado).filter(models.Abre_chamado.id_docente == abre_chamado_id).first()
    if db_abre_chamado is None:
        raise HTTPException(status_code=404, detail="Abre_chamado not found")
    return db_abre_chamado

@router.put("/{abre_chamado_id}", response_model=schemas.Abre_chamado)
def update_abre_chamado(abre_chamado_id: int, abre_chamado: schemas.Abre_chamadoCreate, db: Session = Depends(get_db)):
    db_abre_chamado = db.query(models.Abre_chamado).filter(models.Abre_chamado.id_docente == abre_chamado_id).first()
    if db_abre_chamado is None:
        raise HTTPException(status_code=404, detail="Abre_chamado not found")
    for key, value in abre_chamado.dict().items():
        setattr(db_abre_chamado, key, value)
    db.commit()
    db.refresh(db_abre_chamado)
    return db_abre_chamado

@router.delete("/{abre_chamado_id}", response_model=schemas.Abre_chamado)
def delete_abre_chamado(abre_chamado_id: int, db: Session = Depends(get_db)):
    db_abre_chamado = db.query(models.Abre_chamado).filter(models.Abre_chamado.id_docente == abre_chamado_id).first()
    if db_abre_chamado is None:
        raise HTTPException(status_code=404, detail="Abre_chamado not found")
    db.delete(db_abre_chamado)
    db.commit()
    return db_abre_chamado
