from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    matricula: int

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True

# Você pode criar schemas similares para Docente, Tecnico, Discente, Administrativo, Salas, etc.
