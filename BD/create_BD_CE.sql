CREATE DATABASE IF NOT EXISTS projeto_BD;
USE projeto_BD;

-- Criação das tabelas
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    matricula BIGINT,
    senha VARCHAR(255),
    id_docente INT,
    id_tecnico INT,
    id_discente INT
);

CREATE TABLE Docente (
    id_docente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    matricula BIGINT,
    disciplina VARCHAR(255),
    departamento VARCHAR(255),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Tecnico (
    id_tecnico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    matricula BIGINT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Discente (
    id_discente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    matricula BIGINT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Administrativo (
    id_adm INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    matricula BIGINT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Salas (
    id_sala INT AUTO_INCREMENT PRIMARY KEY,
    sala INT,
    laboratorio VARCHAR(255),
    auditorio VARCHAR(255)
);

CREATE TABLE Agenda (
    id_agenda INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    disciplina VARCHAR(255),
    turma VARCHAR(255),
    quant_alunos INT
);

CREATE TABLE Horarios (
    id_horarios INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_agenda INT,
    id_sala INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_agenda) REFERENCES Agenda(id_agenda),
    FOREIGN KEY (id_sala) REFERENCES Salas(id_sala)
);

CREATE TABLE Visualiza (
    id_docente INT,
    id_discente INT,
    id_tecnico INT,
    id_horarios INT,
    id_adm INT,
    FOREIGN KEY (id_docente) REFERENCES Docente(id_docente),
    FOREIGN KEY (id_discente) REFERENCES Discente(id_discente),
    FOREIGN KEY (id_tecnico) REFERENCES Tecnico(id_tecnico),
    FOREIGN KEY (id_horarios) REFERENCES Horarios(id_horarios),
    FOREIGN KEY (id_adm) REFERENCES Administrativo(id_adm)
);

CREATE TABLE Laboratorio (
    id_lab INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(255),
    id_reserva INT,
    id_chamado INT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Chamado (
    id_chamado INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(255),
    id_lab INT,
    usado_equi VARCHAR(255),
    observacao VARCHAR(255),
    id_usuario INT,
    FOREIGN KEY (id_lab) REFERENCES Laboratorio(id_lab),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Agendamento (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    horario TIME,
    quant_alunos INT,
    observacao VARCHAR(255),
    id_usuario INT,
    id_lab INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_lab) REFERENCES Laboratorio(id_lab)
);

CREATE TABLE Abre_chamado (
    id_docente INT,
    id_lab INT,
    FOREIGN KEY (id_docente) REFERENCES Docente(id_docente),
    FOREIGN KEY (id_lab) REFERENCES Laboratorio(id_lab)
);

CREATE TABLE Gerencia (
    id_tecnico INT,
    id_lab INT,
    FOREIGN KEY (id_tecnico) REFERENCES Tecnico(id_tecnico),
    FOREIGN KEY (id_lab) REFERENCES Laboratorio(id_lab)
);

CREATE TABLE room(
    id_room INT PRIMARY KEY,
    horario TIME NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario)
);