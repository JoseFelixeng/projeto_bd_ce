-- Inserção na tabela Usuario
INSERT INTO Usuario (nome, matricula, senha, id_docente, id_tecnico, id_discente)
VALUES
    ('João Silva', 1234567890, 'senha123', NULL, NULL, NULL),
    ('Maria Oliveira', 2345678901, 'senha456', NULL, NULL, NULL),
    ('Carlos Souza', 3456789012, 'senha789', NULL, NULL, NULL),
    ('Ana Costa', 4567890123, 'senha012', NULL, NULL, NULL),
    ('Pedro Santos', 5678901234, 'senha345', NULL, NULL, NULL);

-- Inserção na tabela Docente
INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario)
VALUES
    ('Dr. Roberto Almeida', 6789012345, 'Matemática', 'Ciências Exatas', 1),
    ('Prof. Laura Pereira', 7890123456, 'Física', 'Ciências Exatas', 2);

-- Inserção na tabela Tecnico
INSERT INTO Tecnico (nome, matricula, id_usuario)
VALUES
    ('José Martins', 8901234567, 3),
    ('Fernanda Lima', 9012345678, 4);

-- Inserção na tabela Discente
INSERT INTO Discente (nome, matricula, id_usuario)
VALUES
    ('Lucas Pereira', 1234509876, 5),
    ('Juliana Costa', 2345610987, 3);

-- Inserção na tabela Administrativo
INSERT INTO Administrativo (nome, matricula, id_usuario)
VALUES
    ('Roberta Silva', 3456709876, 2);

-- Inserção na tabela Salas
INSERT INTO Salas (sala, laboratorio, auditorio)
VALUES
    (101, 'Lab A', 'Auditório 1'),
    (102, 'Lab B', 'Auditório 2');

-- Inserção na tabela Agenda
INSERT INTO Agenda (nome, disciplina, turma, quant_alunos)
VALUES
    ('Matemática - Turma A', 'Matemática', 'A', 30),
    ('Física - Turma B', 'Física', 'B', 25);

-- Inserção na tabela Horarios
INSERT INTO Horarios (id_usuario, id_agenda, id_sala)
VALUES
    (1, 1, 1),
    (2, 2, 2);

-- Inserção na tabela Visualiza
INSERT INTO Visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm)
VALUES
    (1, NULL, NULL, 1, NULL),
    (NULL, 1, NULL, 1, 1);

-- Inserção na tabela Laboratorio
INSERT INTO Laboratorio (status, id_reserva, id_chamado, id_usuario)
VALUES
    ('Disponível', NULL, NULL, 1),
    ('Em Uso', NULL, NULL, 2);

-- Inserção na tabela Chamado
INSERT INTO Chamado (status, id_lab, usado_equi, observacao, id_usuario)
VALUES
    ('Aberto', 1, 'Computador', 'Troca de equipamento', 2),
    ('Fechado', 2, 'Projetor', 'Manutenção concluída', 3);

-- Inserção na tabela Agendamento
INSERT INTO Agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab)
VALUES
    ('2024-09-01', '09:00:00', 30, 'Reunião de equipe', 1, 1),
    ('2024-09-02', '14:00:00', 25, 'Aula de laboratório', 2, 2);

-- Inserção na tabela Abre_chamado
INSERT INTO Abre_chamado (id_docente, id_lab)
VALUES
    (1, 1),
    (2, 2);

-- Inserção na tabela Gerencia
INSERT INTO Gerencia (id_tecnico, id_lab)
VALUES
    (1, 1),
    (2, 2);
