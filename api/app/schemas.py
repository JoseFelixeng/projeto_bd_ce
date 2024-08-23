from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time

class UsuarioBase(BaseModel):
    nome: str
    matricula: int

class UsuarioCreate(UsuarioBase):
    senha: str
    nivel_permissao: Optional[int] = 1 

class Usuario(UsuarioBase):
    id_usuario: int
    nivel_permissao: int
    laboratorios: Optional[List['Laboratorio']] = None
    chamados: Optional[List['Chamado']] = None
    agendamentos: Optional[List['Agendamento']] = None

    class Config:
        from_attributes = True

class DocenteBase(BaseModel):
    nome: str
    matricula: int
    disciplina: str
    departamento: str

class DocenteCreate(DocenteBase):
    id_usuario: int

class Docente(DocenteBase):
    id_docente: int

    class Config:
        from_attributes = True

class TecnicoBase(BaseModel):
    nome: str
    matricula: int

class TecnicoCreate(TecnicoBase):
    id_usuario: int

class Tecnico(TecnicoBase):
    id_tecnico: int

    class Config:
        from_attributes = True

class DiscenteBase(BaseModel):
    nome: str
    matricula: int

class DiscenteCreate(DiscenteBase):
    id_usuario: int

class Discente(DiscenteBase):
    id_discente: int

    class Config:
        from_attributes = True

class AdministrativoBase(BaseModel):
    nome: str
    matricula: int

class AdministrativoCreate(AdministrativoBase):
    id_usuario: int

class Administrativo(AdministrativoBase):
    id_adm: int

    class Config:
        from_attributes = True

class SalasBase(BaseModel):
    sala: int
    laboratorio: str
    auditorio: str

class SalasCreate(SalasBase):
    pass

class Salas(SalasBase):
    id_sala: int

    class Config:
        from_attributes = True

class AgendaBase(BaseModel):
    nome: str
    disciplina: str
    turma: str
    quant_alunos: int

class AgendaCreate(AgendaBase):
    pass

class Agenda(AgendaBase):
    id_agenda: int

    class Config:
        from_attributes = True

class HorariosBase(BaseModel):
    id_usuario: int
    id_agenda: int
    id_sala: int

class HorariosCreate(HorariosBase):
    pass

class Horarios(HorariosBase):
    id_horarios: int

    class Config:
        from_attributes = True

class VisualizaBase(BaseModel):
    id_docente: Optional[int]
    id_discente: Optional[int]
    id_tecnico: Optional[int]
    id_horarios: Optional[int]
    id_adm: Optional[int]

class VisualizaCreate(VisualizaBase):
    pass

class Visualiza(VisualizaBase):
    pass

    class Config:
        from_attributes = True

class LaboratorioBase(BaseModel):
    status: str
    id_reserva: Optional[int]
    id_chamado: Optional[int]
    id_usuario: int

class LaboratorioCreate(LaboratorioBase):
    pass

class Laboratorio(LaboratorioBase):
    id_lab: int

    class Config:
        from_attributes = True

class ChamadoBase(BaseModel):
    status: str
    id_lab: int
    usado_equi: str
    observacao: str
    id_usuario: int

class ChamadoCreate(ChamadoBase):
    pass

class Chamado(ChamadoBase):
    id_chamado: int

    class Config:
        from_attributes = True

class AgendamentoBase(BaseModel):
    data: date  # Usando 'date' para a data
    horario: time  # Usando 'time' para o horário
    quant_alunos: int
    observacao: str
    id_usuario: int
    id_lab: int

class AgendamentoCreate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    id_reserva: int

    class Config:
        from_attributes = True

class AbreChamadoBase(BaseModel):
    id_docente: int
    id_lab: int

class AbreChamadoCreate(AbreChamadoBase):
    pass

class AbreChamado(AbreChamadoBase):
    pass

    class Config:
        from_attributes = True

class GerenciaBase(BaseModel):
    id_tecnico: int
    id_lab: int

class GerenciaCreate(GerenciaBase):
    pass

class Gerencia(GerenciaBase):
    pass

    class Config:
        from_attributes = True

class RoomBase(BaseModel):
    horario: str
    id_usuario: int

class RoomCreate(BaseModel):
    id_room: int
    horario: str
    id_usuario: int

class Room(RoomBase):
    id_room: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UsuarioLogin(BaseModel):
    matricula: int
    senha: str
