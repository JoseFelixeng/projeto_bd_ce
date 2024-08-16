from fastapi import APIRouter, Depends, HTTPException, status
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

@router.post("/usuario", response_model=schemas.Usuario, status_code=status.HTTP_201_CREATED)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica se já existe um usuário com a mesma matrícula
    db_usuario = db.query(models.Usuario).filter(models.Usuario.matricula == usuario.matricula).first()
    if db_usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Matrícula já registrada")
    
    # Cria um novo usuário
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/usuario/{usuario_id}", response_model=schemas.Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    return db_usuario

@router.put("/usuario/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    
    # Atualiza os atributos do usuário
    for key, value in usuario.dict().items():
        setattr(db_usuario, key, value)
    
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.delete("/usuario/{usuario_id}", response_model=schemas.Usuario)
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    
    db.delete(db_usuario)
    db.commit()
    return db_usuario
