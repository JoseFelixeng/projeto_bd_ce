from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
import aiomysql
import asyncio

app = FastAPI()

# Configuração do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'rasengan',
    'db': 'projetoBD'
}


class administrativo(BaseModel):
    id: int
    nome: str
    matricula: str
    id_usuario: int 

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union [str, None] = None ):
    return {"item_id" : item.name}