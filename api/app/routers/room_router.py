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

@router.post("/", response_model=schemas.Room)
def update_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    if room.id_room not in [1, 2, 3, 4]:
        raise HTTPException(status_code=400, detail="Invalid room ID. Only IDs 1 to 4 are allowed.")
    
    db_room = db.query(models.Room).filter(models.Room.id_room == room.id_room).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")

    db_room.horario = room.horario
    db_room.id_usuario = room.id_usuario
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/room/{room_id}", response_model=schemas.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id_room == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@router.put("/room/{room_id}", response_model=schemas.Room)
def update_room(room_id: int, room: schemas.RoomCreate, db: Session = Depends(get_db)):
    if room_id not in [1, 2, 3, 4]:
        raise HTTPException(status_code=400, detail="Invalid room ID. Only IDs 1 to 4 are allowed.")
    
    db_room = db.query(models.Room).filter(models.Room.id_room == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")

    db_room.horario = room.horario
    db_room.id_usuario = room.id_usuario
    db.commit()
    db.refresh(db_room)
    return db_room

@router.delete("/room/{room_id}", response_model=schemas.Room)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id_room == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(db_room)
    db.commit()
    return db_room
