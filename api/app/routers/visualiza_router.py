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

@router.post("/visualiza/", response_model=schemas.Visualiza)
def create_visualiza(visualiza: schemas.VisualizaCreate, db: Session = Depends(get_db)):
    db_visualiza = models.Visualiza(**visualiza.dict())
    db.add(db_visualiza)
    db.commit()
    db.refresh(db_visualiza)
    return db_visualiza

@router.get("/{visualiza_id}", response_model=schemas.Visualiza)
def read_visualiza(visualiza_id: int, db: Session = Depends(get_db)):
    db_visualiza = db.query(models.Visualiza).filter(models.Visualiza.id_horarios == visualiza_id).first()
    if db_visualiza is None:
        raise HTTPException(status_code=404, detail="Visualiza not found")
    return db_visualiza

@router.put("/{visualiza_id}", response_model=schemas.Visualiza)
def update_visualiza(visualiza_id: int, visualiza: schemas.VisualizaCreate, db: Session = Depends(get_db)):
    db_visualiza = db.query(models.Visualiza).filter(models.Visualiza.id_horarios == visualiza_id).first()
    if db_visualiza is None:
        raise HTTPException(status_code=404, detail="Visualiza not found")
    for key, value in visualiza.dict().items():
        setattr(db_visualiza, key, value)
    db.commit()
    db.refresh(db_visualiza)
    return db_visualiza

@router.delete("/{visualiza_id}", response_model=schemas.Visualiza)
def delete_visualiza(visualiza_id: int, db: Session = Depends(get_db)):
    db_visualiza = db.query(models.Visualiza).filter(models.Visualiza.id_horarios == visualiza_id).first()
    if db_visualiza is None:
        raise HTTPException(status_code=404, detail="Visualiza not found")
    db.delete(db_visualiza)
    db.commit()
    return db_visualiza
