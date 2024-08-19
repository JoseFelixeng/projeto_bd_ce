from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "mariadb+mariadbconnector://root:rasengan@localhost/projetoBD"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    senha = Column(String(255))

    docente = relationship("Docente", uselist=False, back_populates="usuario")
    tecnico = relationship("Tecnico", uselist=False, back_populates="usuario")
    discente = relationship("Discente", uselist=False, back_populates="usuario")
    administrativo = relationship("Administrativo", uselist=False, back_populates="usuario")
    laboratorios = relationship("Laboratorio", back_populates="usuario")
    chamados = relationship("Chamado", back_populates="usuario")
    agendamentos = relationship("Agendamento", back_populates="usuario")

class Docente(Base):
    __tablename__ = 'Docente'
    id_docente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    disciplina = Column(String(255))
    departamento = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    
    usuario = relationship("Usuario", back_populates="docente")

class Tecnico(Base):
    __tablename__ = 'Tecnico'
    id_tecnico = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    
    usuario = relationship("Usuario", back_populates="tecnico")

class Discente(Base):
    __tablename__ = 'Discente'
    id_discente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    
    usuario = relationship("Usuario", back_populates="discente")

class Administrativo(Base):
    __tablename__ = 'Administrativo'
    id_adm = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    matricula = Column(Integer, unique=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    
    usuario = relationship("Usuario", back_populates="administrativo")

class Salas(Base):
    __tablename__ = 'Salas'
    id_sala = Column(Integer, primary_key=True, index=True)
    sala = Column(Integer)
    laboratorio = Column(String(255))
    auditorio = Column(String(255))

class Agenda(Base):
    __tablename__ = 'Agenda'
    id_agenda = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    disciplina = Column(String(255))
    turma = Column(String(255))
    quant_alunos = Column(Integer)

class Horarios(Base):
    __tablename__ = 'Horarios'
    id_horarios = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    id_agenda = Column(Integer, ForeignKey('Agenda.id_agenda'))
    id_sala = Column(Integer, ForeignKey('Salas.id_sala'))

    usuario = relationship("Usuario")
    agenda = relationship("Agenda")
    sala = relationship("Salas")

class Visualiza(Base):
    __tablename__ = 'Visualiza'
    id_docente = Column(Integer, ForeignKey('Docente.id_docente'), primary_key=True)
    id_discente = Column(Integer, ForeignKey('Discente.id_discente'), primary_key=True)
    id_tecnico = Column(Integer, ForeignKey('Tecnico.id_tecnico'), primary_key=True)
    id_horarios = Column(Integer, ForeignKey('Horarios.id_horarios'), primary_key=True)
    id_adm = Column(Integer, ForeignKey('Administrativo.id_adm'), primary_key=True)

    docente = relationship("Docente")
    discente = relationship("Discente")
    tecnico = relationship("Tecnico")
    horarios = relationship("Horarios")
    administrativo = relationship("Administrativo")

class Laboratorio(Base):
    __tablename__ = 'Laboratorio'
    id_lab = Column(Integer, primary_key=True, index=True)
    status = Column(String(255))

    usuario = relationship("Usuario", back_populates="laboratorios")
    chamados = relationship("Chamado", back_populates="laboratorio")
    agendamentos = relationship("Agendamento", back_populates="laboratorio")

class Chamado(Base):
    __tablename__ = 'Chamado'
    id_chamado = Column(Integer, primary_key=True, index=True)
    status = Column(String(255))
    id_lab = Column(Integer, ForeignKey('Laboratorio.id_lab'))
    usado_equi = Column(String(255))
    observacao = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))

    laboratorio = relationship("Laboratorio", back_populates="chamados")
    usuario = relationship("Usuario", back_populates="chamados")

class Agendamento(Base):
    __tablename__ = 'Agendamento'
    id_reserva = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    horario = Column(Time)
    quant_alunos = Column(Integer)
    observacao = Column(String(255))
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    id_lab = Column(Integer, ForeignKey('Laboratorio.id_lab'))

    usuario = relationship("Usuario", back_populates="agendamentos")
    laboratorio = relationship("Laboratorio", back_populates="agendamentos")

class Abre_chamado(Base):
    __tablename__ = 'Abre_chamado'
    id_docente = Column(Integer, ForeignKey('Docente.id_docente'), primary_key=True)
    id_lab = Column(Integer, ForeignKey('Laboratorio.id_lab'))

    docente = relationship("Docente")
    laboratorio = relationship("Laboratorio")

class Gerencia(Base):
    __tablename__ = 'Gerencia'
    id_tecnico = Column(Integer, ForeignKey('Tecnico.id_tecnico'), primary_key=True)
    id_lab = Column(Integer, ForeignKey('Laboratorio.id_lab'))

    tecnico = relationship("Tecnico")
    laboratorio = relationship("Laboratorio")

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)
