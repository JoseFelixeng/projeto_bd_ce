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



