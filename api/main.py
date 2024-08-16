from fastapi import FastAPI
from app import router, models, database

app = FastAPI()

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

app.include_router(router.router)

# Adicione outras rotas ou middlewares conforme necessário
