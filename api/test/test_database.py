# tests/test_database.py

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Usuario

def test_database_connection():
    # Tente abrir uma sessão
    try:
        session = SessionLocal()
        assert session is not None
    finally:
        session.close()

def test_create_and_retrieve_user():
    session = SessionLocal()
    new_user = Usuario(nome="Jane Doe", matricula=54321, senha="password123")
    session.add(new_user)
    session.commit()

    retrieved_user = session.query(Usuario).filter(Usuario.matricula == 54321).first()
    assert retrieved_user is not None
    assert retrieved_user.nome == "Jane Doe"
    assert retrieved_user.matricula == 54321

    session.delete(retrieved_user)
    session.commit()
    session.close()
