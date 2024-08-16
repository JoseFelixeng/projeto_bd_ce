from pydantic import BaseModel
from typing import Optional, List

class UsuarioBase(BaseModel):
    nome: str
    matricula: int

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id_usuario: int

    class Config:
        orm_mode = True

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
        orm_mode = True

class TecnicoBase(BaseModel):
    nome: str
    matricula: int

class TecnicoCreate(TecnicoBase):
    id_usuario: int

class Tecnico(TecnicoBase):
    id_tecnico: int

    class Config:
        orm_mode = True

class DiscenteBase(BaseModel):
    nome: str
    matricula: int

class DiscenteCreate(DiscenteBase):
    id_usuario: int

class Discente(DiscenteBase):
    id_discente: int

    class Config:
        orm_mode = True

class AdministrativoBase(BaseModel):
    nome: str
    matricula: int

class AdministrativoCreate(AdministrativoBase):
    id_usuario: int

class Administrativo(AdministrativoBase):
    id_adm: int

    class Config:
        orm_mode = True

class SalasBase(BaseModel):
    sala: int
    laboratorio: str
    auditorio: str

class SalasCreate(SalasBase):
    pass

class Salas(SalasBase):
    id_sala: int

    class Config:
        orm_mode = True

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
        orm_mode = True

class HorariosBase(BaseModel):
    id_usuario: int
    id_agenda: int
    id_sala: int

class HorariosCreate(HorariosBase):
    pass

class Horarios(HorariosBase):
    id_horarios: int

    class Config:
        orm_mode = True

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
        orm_mode = True

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
        orm_mode = True

class AgendamentoBase(BaseModel):
    data: str
    horario: str
    quant_alunos: int
    observacao: str
    id_usuario: int
    id_lab: int

class AgendamentoCreate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    id_reserva: int

    class Config:
        orm_mode = True

class AbreChamadoBase(BaseModel):
    id_docente: int
    id_lab: int

class AbreChamadoCreate(AbreChamadoBase):
    pass

class AbreChamado(AbreChamadoBase):
    pass

class GerenciaBase(BaseModel):
    id_tecnico: int
    id_lab: int

class GerenciaCreate(GerenciaBase):
    pass

class Gerencia(GerenciaBase):
    pass
