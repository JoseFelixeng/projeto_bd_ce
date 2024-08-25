from fastapi import FastAPI
from .routers import usuario_router, docente_router, tecnico_router, discente_router, sala_router, agenda_router, horarios_router, visualiza_router, chamado_router, agendamento_router, abre_chamado_router, gerencia_router, room_router, contagem_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Banco de Dados")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(usuario_router.router,prefix="/user", tags=['Usuario'])
app.include_router(docente_router.router,prefix="/docente", tags=['Docente'])
app.include_router(tecnico_router.router,prefix="/tecnico", tags=['Tecnico'])
app.include_router(discente_router.router,prefix="/discente", tags=['Discente'])
app.include_router(sala_router.router,prefix="/sala", tags=['Sala'])
app.include_router(agenda_router.router,prefix="/agenda", tags=['Agenda'])
app.include_router(horarios_router.router,prefix="/horarios", tags=['Horarios'])
app.include_router(visualiza_router,prefix="/visualizar", tags=['Visualizar'])
app.include_router(chamado_router.router,prefix="/chamado", tags=['Chamado'])
app.include_router(agendamento_router.router,prefix="/agendamento", tags=['Agendamento'])
app.include_router(abre_chamado_router.router,prefix="/abre_chamado", tags=['Abre chamado'])
app.include_router(gerencia_router.router,prefix="/gerencia", tags=['Gerencia']) 
app.include_router(room_router.router,prefix="/room", tags=['Room'])
app.include_router(contagem_router.router, prefix="/count", tags=['Count'])
