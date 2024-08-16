# tests/test_models.py

from app.models import Usuario

def test_create_user():
    user = Usuario(nome="John Doe", matricula=12345, senha="password")
    assert user.nome == "John Doe"
    assert user.matricula == 12345
    assert user.senha == "password"
