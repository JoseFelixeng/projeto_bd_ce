from fastapi import FastAPI
from .routers import usuario_router, docente_router, tecnico_router, discente_router, sala_router, agenda_router, horarios_router, visualiza_router, chamado_router, agendamento_router, abre_chamado_router, gerencia_router

app = FastAPI()

app.include_router(usuario_router.router)
app.include_router(docente_router.router)
app.include_router(tecnico_router.router)
app.include_router(discente_router.router)
app.include_router(sala_router.router)
app.include_router(agenda_router.router)
app.include_router(horarios_router.router)
app.include_router(visualiza_router.router)
app.include_router(chamado_router.router)
app.include_router(agendamento_router.router)
app.include_router(abre_chamado_router.router)
app.include_router(gerencia_router.router)
