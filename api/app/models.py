from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    senha = Column(String(255))
    docentes = relationship("Docente", back_populates="usuario")
    tecnicos = relationship("Tecnico", back_populates="usuario")
    discentes = relationship("Discente", back_populates="usuario")
    administrativos = relationship("Administrativo", back_populates="usuario")

class Docente(Base):
    __tablename__ = 'docente'

    id_docente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    disciplina = Column(String(255))
    departamento = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="docentes")

class Tecnico(Base):
    __tablename__ = 'tecnico'

    id_tecnico = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="tecnicos")

class Discente(Base):
    __tablename__ = 'discente'

    id_discente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="discentes")

class Administrativo(Base):
    __tablename__ = 'administrativo'

    id_adm = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="administrativos")

class Salas(Base):
    __tablename__ = 'salas'

    id_sala = Column(Integer, primary_key=True, index=True)
    sala = Column(Integer)
    laboratorio = Column(String(255))
    auditorio = Column(String(255))

class Agenda(Base):
    __tablename__ = 'agenda'

    id_agenda = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    disciplina = Column(String(255))
    turma = Column(String(255))
    quant_alunos = Column(Integer)

class Horarios(Base):
    __tablename__ = 'horarios'

    id_horarios = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_agenda = Column(Integer, ForeignKey('agenda.id_agenda'))
    id_sala = Column(Integer, ForeignKey('salas.id_sala'))

class Visualiza(Base):
    __tablename__ = 'visualiza'

    id_docente = Column(Integer, ForeignKey('docente.id_docente'), primary_key=True)
    id_discente = Column(Integer, ForeignKey('discente.id_discente'), primary_key=True)
    id_tecnico = Column(Integer, ForeignKey('tecnico.id_tecnico'), primary_key=True)
    id_horarios = Column(Integer, ForeignKey('horarios.id_horarios'), primary_key=True)
    id_adm = Column(Integer, ForeignKey('administrativo.id_adm'), primary_key=True)

class Laboratorio(Base):
    __tablename__ = 'laboratorio'

    id_lab = Column(Integer, primary_key=True, index=True)
    status = Column(String(255))
    id_reserva = Column(Integer)
    id_chamado = Column(Integer)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))

class Chamado(Base):
    __tablename__ = 'chamado'

    id_chamado = Column(Integer, primary_key=True, index=True)
    status = Column(String(255))
    id_lab = Column(Integer, ForeignKey('laboratorio.id_lab'))
    usado_equi = Column(String(255))
    observacao = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))

class Agendamento(Base):
    __tablename__ = 'agendamento'

    id_reserva = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    horario = Column(Time)
    quant_alunos = Column(Integer)
    observacao = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_lab = Column(Integer, ForeignKey('laboratorio.id_lab'))

class Abre_chamado(Base):
    __tablename__ = 'abre_chamado'

    id_docente = Column(Integer, ForeignKey('docente.id_docente'), primary_key=True)
    id_lab = Column(Integer, ForeignKey('laboratorio.id_lab'), primary_key=True)

class Gerencia(Base):
    __tablename__ = 'gerencia'

    id_tecnico = Column(Integer, ForeignKey('tecnico.id_tecnico'), primary_key=True)
    id_lab = Column(Integer, ForeignKey('laboratorio.id_lab'), primary_key=True)
