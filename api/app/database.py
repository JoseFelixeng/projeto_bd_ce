from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração da URL do banco de dados para MariaDB
DATABASE_URL = "mariadb+mariadbconnector://root:root@localhost:3309/projetoBD"

# Criando o engine para conectar com o banco de dados
engine = create_engine(DATABASE_URL, echo=True)

# Criando uma sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
