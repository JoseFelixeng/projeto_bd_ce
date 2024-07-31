from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
import aiomysql
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite qualquer método HTTP
    allow_headers=["*"],  # Permite qualquer cabeçalho
)

# Configuração do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'rasengan',
    'db': 'projetoBD'
}

# Configuração do passlib para criptografia de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para obter a conexão com o banco de dados
async def get_db_connection():
    return await aiomysql.connect(**DB_CONFIG)

# Modelos de dados
class User(BaseModel):
    nome: str
    matricula: int
    senha: str
    tipo: int  # Tipo do usuário: 1=Professor, 2=Aluno, 4=Técnico

class Docente(BaseModel):
    nome: str
    matricula: int
    disciplina: str
    departamento: str
    id_usuario: int

class Tecnico(BaseModel):
    nome: str
    matricula: int
    id_usuario: int

class Discente(BaseModel):
    nome: str
    matricula: int
    id_usuario: int

class Administrativo(BaseModel):
    nome: str
    matricula: int
    id_usuario: int

class Sala(BaseModel):
    sala: int
    laboratorio: str
    auditorio: str

class Agenda(BaseModel):
    nome: str
    disciplina: str
    turma: str
    quant_alunos: int

class Horario(BaseModel):
    id_usuario: int
    id_agenda: int
    id_sala: int

class Visualiza(BaseModel):
    id_docente: int
    id_discente: int
    id_tecnico: int
    id_horarios: int
    id_adm: int

class Laboratorio(BaseModel):
    status: str
    id_reserva: int
    id_chamado: int
    id_usuario: int

class Chamado(BaseModel):
    status: str
    id_lab: int
    usado_equi: str
    observacao: str
    id_usuario: int

class Agendamento(BaseModel):
    data: str
    horario: str
    quant_alunos: int
    observacao: str
    id_usuario: int
    id_lab: int

class AbreChamado(BaseModel):
    id_docente: int
    id_lab: int

class Gerencia(BaseModel):
    id_tecnico: int
    id_lab: int

@app.post("/cadastro/")
async def create_user(user: User):
    hashed_password = pwd_context.hash(user.senha)
    
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir o novo usuário na tabela
            await cursor.execute(
                "INSERT INTO usuario (nome, matricula, senha, tipo) VALUES (%s, %s, %s, %s)",
                (user.nome, user.matricula, hashed_password, user.tipo)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar usuário: {str(e)}")
        finally:
            connection.close()

    return {"status": "Usuário cadastrado com sucesso"}

@app.post("/login/")
async def login(user: User):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        # Buscar usuário pelo nome
        await cursor.execute("SELECT senha, tipo FROM usuario WHERE nome=%s", (user.nome,))
        result = await cursor.fetchone()
        
        if result is None:
            await connection.close()
            raise HTTPException(status_code=400, detail="Usuário não encontrado.")
        
        db_password, user_type = result
        
        # Verificar se a senha está correta
        if not pwd_context.verify(user.senha, db_password):
            await connection.close()
            raise HTTPException(status_code=400, detail="Senha incorreta.")
        
        await connection.close()

        return {"type": user_type}

@app.post("/docente/")
async def create_docente(docente: Docente):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo docente
            await cursor.execute(
                "INSERT INTO docente (nome, matricula, disciplina, departamento, id_usuario) VALUES (%s, %s, %s, %s, %s)",
                (docente.nome, docente.matricula, docente.disciplina, docente.departamento, docente.id_usuario)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar docente: {str(e)}")
        finally:
            connection.close()

    return {"status": "Docente cadastrado com sucesso"}

@app.post("/tecnico/")
async def create_tecnico(tecnico: Tecnico):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo técnico
            await cursor.execute(
                "INSERT INTO tecnico (nome, matricula, id_usuario) VALUES (%s, %s, %s)",
                (tecnico.nome, tecnico.matricula, tecnico.id_usuario)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar técnico: {str(e)}")
        finally:
            connection.close()

    return {"status": "Técnico cadastrado com sucesso"}

@app.post("/discente/")
async def create_discente(discente: Discente):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo discente
            await cursor.execute(
                "INSERT INTO discente (nome, matricula, id_usuario) VALUES (%s, %s, %s)",
                (discente.nome, discente.matricula, discente.id_usuario)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar discente: {str(e)}")
        finally:
            connection.close()

    return {"status": "Discente cadastrado com sucesso"}

@app.post("/administrativo/")
async def create_administrativo(administrativo: Administrativo):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo administrativo
            await cursor.execute(
                "INSERT INTO administrativo (nome, matricula, id_usuario) VALUES (%s, %s, %s)",
                (administrativo.nome, administrativo.matricula, administrativo.id_usuario)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar administrativo: {str(e)}")
        finally:
            connection.close()

    return {"status": "Administrativo cadastrado com sucesso"}

@app.post("/salas/")
async def create_sala(sala: Sala):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir nova sala
            await cursor.execute(
                "INSERT INTO salas (sala, laboratorio, auditorio) VALUES (%s, %s, %s)",
                (sala.sala, sala.laboratorio, sala.auditorio)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar sala: {str(e)}")
        finally:
            connection.close()

    return {"status": "Sala cadastrada com sucesso"}

@app.post("/agenda/")
async def create_agenda(agenda: Agenda):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir nova agenda
            await cursor.execute(
                "INSERT INTO agenda (nome, disciplina, turma, quant_alunos) VALUES (%s, %s, %s, %s)",
                (agenda.nome, agenda.disciplina, agenda.turma, agenda.quant_alunos)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar agenda: {str(e)}")
        finally:
            connection.close()

    return {"status": "Agenda cadastrada com sucesso"}

@app.post("/horarios/")
async def create_horario(horario: Horario):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo horário
            await cursor.execute(
                "INSERT INTO horarios (id_usuario, id_agenda, id_sala) VALUES (%s, %s, %s)",
                (horario.id_usuario, horario.id_agenda, horario.id_sala)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar horário: {str(e)}")
        finally:
            connection.close()

    return {"status": "Horário cadastrado com sucesso"}

@app.post("/visualiza/")
async def create_visualiza(visualiza: Visualiza):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo visualização
            await cursor.execute(
                "INSERT INTO visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm) VALUES (%s, %s, %s, %s, %s)",
                (visualiza.id_docente, visualiza.id_discente, visualiza.id_tecnico, visualiza.id_horarios, visualiza.id_adm)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar visualização: {str(e)}")
        finally:
            connection.close()

    return {"status": "Visualização cadastrada com sucesso"}

@app.post("/laboratorio/")
async def create_laboratorio(laboratorio: Laboratorio):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo laboratório
            await cursor.execute(
                "INSERT INTO laboratorio (status, id_reserva, id_chamado, id_usuario) VALUES (%s, %s, %s, %s)",
                (laboratorio.status, laboratorio.id_reserva, laboratorio.id_chamado, laboratorio.id_usuario)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar laboratório: {str(e)}")
        finally:
            connection.close()

    return {"status": "Laboratório cadastrado com sucesso"}

@app.post("/chamado/")
async def create_chamado(chamado: Chamado):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo chamado
            await cursor.execute(
                "INSERT INTO chamado (status, id_lab, usado_equi, observacao, id_usuario) VALUES (%s, %s, %s, %s, %s)",
                (chamado.status, chamado.id_lab, chamado.usado_equi, chamado.observacao, chamado.id_usuario)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar chamado: {str(e)}")
        finally:
            connection.close()

    return {"status": "Chamado cadastrado com sucesso"}

@app.post("/agendamento/")
async def create_agendamento(agendamento: Agendamento):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo agendamento
            await cursor.execute(
                "INSERT INTO agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab) VALUES (%s, %s, %s, %s, %s, %s)",
                (agendamento.data, agendamento.horario, agendamento.quant_alunos, agendamento.observacao, agendamento.id_usuario, agendamento.id_lab)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar agendamento: {str(e)}")
        finally:
            connection.close()

    return {"status": "Agendamento cadastrado com sucesso"}

@app.post("/abre_chamado/")
async def create_abre_chamado(abre_chamado: AbreChamado):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir novo abre_chamado
            await cursor.execute(
                "INSERT INTO abre_chamado (id_docente, id_lab) VALUES (%s, %s)",
                (abre_chamado.id_docente, abre_chamado.id_lab)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar abertura de chamado: {str(e)}")
        finally:
            connection.close()

    return {"status": "Abertura de chamado cadastrada com sucesso"}

@app.post("/gerencia/")
async def create_gerencia(gerencia: Gerencia):
    connection = await get_db_connection()
    async with connection.cursor() as cursor:
        try:
            # Inserir nova gerência
            await cursor.execute(
                "INSERT INTO gerencia (id_tecnico, id_lab) VALUES (%s, %s)",
                (gerencia.id_tecnico, gerencia.id_lab)
            )
            await connection.commit()
        except Exception as e:
            await connection.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao cadastrar gerência: {str(e)}")
        finally:
            connection.close()

    return {"status": "Gerência cadastrada com sucesso"}
