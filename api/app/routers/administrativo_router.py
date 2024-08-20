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

@router.post("/administrativo/", response_model=schemas.Administrativo)
def create_administrativo(administrativo: schemas.AdministrativoCreate, db: Session = Depends(get_db)):
    db_administrativo = models.Administrativo(**administrativo.dict())
    db.add(db_administrativo)
    db.commit()
    db.refresh(db_administrativo)
    return db_administrativo

@router.get("/administrativo/{administrativo_id}", response_model=schemas.Administrativo)
def read_administrativo(administrativo_id: int, db: Session = Depends(get_db)):
    db_administrativo = db.query(models.Administrativo).filter(models.Administrativo.id_adm == administrativo_id).first()
    if db_administrativo is None:
        raise HTTPException(status_code=404, detail="Administrativo not found")
    return db_administrativo

@router.put("/administrativo/{administrativo_id}", response_model=schemas.Administrativo)
def update_administrativo(administrativo_id: int, administrativo: schemas.AdministrativoCreate, db: Session = Depends(get_db)):
    db_administrativo = db.query(models.Administrativo).filter(models.Administrativo.id_adm == administrativo_id).first()
    if db_administrativo is None:
        raise HTTPException(status_code=404, detail="Administrativo not found")
    for key, value in administrativo.dict().items():
        setattr(db_administrativo, key, value)
    db.commit()
    db.refresh(db_administrativo)
    return db_administrativo

@router.delete("/administrativo/{administrativo_id}", response_model=schemas.Administrativo)
def delete_administrativo(administrativo_id: int, db: Session = Depends(get_db)):
    db_administrativo = db.query(models.Administrativo).filter(models.Administrativo.id_adm == administrativo_id).first()
    if db_administrativo is None:
        raise HTTPException(status_code=404, detail="Administrativo not found")
    db.delete(db_administrativo)
    db.commit()
    return db_administrativo
