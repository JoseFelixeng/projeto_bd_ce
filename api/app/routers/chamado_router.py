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

@router.post("/chamado/", response_model=schemas.Chamado)
def create_chamado(chamado: schemas.ChamadoCreate, db: Session = Depends(get_db)):
    db_chamado = models.Chamado(**chamado.dict())
    db.add(db_chamado)
    db.commit()
    db.refresh(db_chamado)
    return db_chamado

@router.get("/chamado/{chamado_id}", response_model=schemas.Chamado)
def read_chamado(chamado_id: int, db: Session = Depends(get_db)):
    db_chamado = db.query(models.Chamado).filter(models.Chamado.id_chamado == chamado_id).first()
    if db_chamado is None:
        raise HTTPException(status_code=404, detail="Chamado not found")
    return db_chamado

@router.put("/chamado/{chamado_id}", response_model=schemas.Chamado)
def update_chamado(chamado_id: int, chamado: schemas.ChamadoCreate, db: Session = Depends(get_db)):
    db_chamado = db.query(models.Chamado).filter(models.Chamado.id_chamado == chamado_id).first()
    if db_chamado is None:
        raise HTTPException(status_code=404, detail="Chamado not found")
    for key, value in chamado.dict().items():
        setattr(db_chamado, key, value)
    db.commit()
    db.refresh(db_chamado)
    return db_chamado

@router.delete("/chamado/{chamado_id}", response_model=schemas.Chamado)
def delete_chamado(chamado_id: int, db: Session = Depends(get_db)):
    db_chamado = db.query(models.Chamado).filter(models.Chamado.id_chamado == chamado_id).first()
    if db_chamado is None:
        raise HTTPException(status_code=404, detail="Chamado not found")
    db.delete(db_chamado)
    db.commit()
    return db_chamado
