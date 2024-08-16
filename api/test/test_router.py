# tests/test_router.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"nome": "John Doe", "matricula": 12345, "senha": "password"})
    assert response.status_code == 200
    assert response.json()["nome"] == "John Doe"
    assert response.json()["matricula"] == 12345
