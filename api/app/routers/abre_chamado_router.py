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

@router.post("/abre/", response_model=schemas.AbreChamadoCreate)
def create_abre_chamado(abre_chamado: schemas.AbreChamadoCreate, db: Session = Depends(get_db)):
    db_abre_chamado = models.Abre_chamado(**abrechamado.dict())
    db.add(db_abre_chamado)
    db.commit()
    db.refresh(db_abre_chamado)
    return db_abre_chamado

@router.get("/abre/{abre_chamado_id}", response_model=schemas.AbreChamadoBase)
def read_abre_chamado(abre_chamado_id: int, db: Session = Depends(get_db)):
    db_abre_chamado = db.query(models.Abre_chamado).filter(models.Abre_chamado.id_docente == abre_chamado_id).first()
    if db_abre_chamado is None:
        raise HTTPException(status_code=404, detail="Abre_chamado not found")
    return db_abre_chamado

@router.put("/abre/{abre_chamado_id}", response_model=schemas.AbreChamado)
def update_abre_chamado(abre_chamado_id: int, abre_chamado: schemas.AbreChamadoCreate, db: Session = Depends(get_db)):
    db_abre_chamado = db.query(models.Abre_chamado).filter(models.Abre_chamado.id_docente == abre_chamado_id).first()
    if db_abre_chamado is None:
        raise HTTPException(status_code=404, detail="Abre_chamado not found")
    for key, value in abre_chamado.dict().items():
        setattr(db_abre_chamado, key, value)
    db.commit()
    db.refresh(db_abre_chamado)
    return db_abre_chamado

@router.delete("/abre/{abre_chamado_id}", response_model=schemas.AbreChamado)
def delete_abre_chamado(abre_chamado_id: int, db: Session = Depends(get_db)):
    db_abre_chamado = db.query(models.Abre_chamado).filter(models.Abre_chamado.id_docente == abre_chamado_id).first()
    if db_abre_chamado is None:
        raise HTTPException(status_code=404, detail="Abre_chamado not found")
    db.delete(db_abre_chamado)
    db.commit()
    return db_abre_chamado
