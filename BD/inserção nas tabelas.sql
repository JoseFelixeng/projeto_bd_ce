-- Inserções na tabela Usuario
INSERT INTO Usuario (nome, matricula, senha) VALUES ('João Silva', 201800001, 'senha123');
INSERT INTO Usuario (nome, matricula, senha) VALUES ('Maria Oliveira', 201800002, 'senha456');

-- Inserções na tabela Docente
INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario) VALUES ('Dr. Pedro Santos', 1001, 'Matemática', 'Ciências Exatas', 1);
INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario) VALUES ('Dra. Ana Costa', 1002, 'Física', 'Ciências Exatas', 2);

-- Inserções na tabela Tecnico
INSERT INTO Tecnico (nome, matricula, id_usuario) VALUES ('Carlos Pereira', 2001, 1);
INSERT INTO Tecnico (nome, matricula, id_usuario) VALUES ('Fernanda Lima', 2002, 2);

-- Inserções na tabela Discente
INSERT INTO Discente (nome, matricula, id_usuario) VALUES ('Lucas Almeida', 3001, 1);
INSERT INTO Discente (nome, matricula, id_usuario) VALUES ('Juliana Santos', 3002, 2);

-- Inserções na tabela Administrativo
INSERT INTO Administrativo (nome, matricula, id_usuario) VALUES ('Ana Paula', 4001, 1);
INSERT INTO Administrativo (nome, matricula, id_usuario) VALUES ('Bruno Martins', 4002, 2);

-- Inserções na tabela Salas
INSERT INTO Salas (sala, laboratorio, auditorio) VALUES (101, 'Lab A', 'Auditório 1');
INSERT INTO Salas (sala, laboratorio, auditorio) VALUES (102, 'Lab B', 'Auditório 2');

-- Inserções na tabela Agenda
INSERT INTO Agenda (nome, disciplina, turma, quant_alunos) VALUES ('Matemática I', 'Matemática', 'Turma A', 30);
INSERT INTO Agenda (nome, disciplina, turma, quant_alunos) VALUES ('Física I', 'Física', 'Turma B', 25);

-- Inserções na tabela Horarios
INSERT INTO Horarios (id_usuario, id_agenda, id_sala) VALUES (1, 1, 1);
INSERT INTO Horarios (id_usuario, id_agenda, id_sala) VALUES (2, 2, 2);

-- Inserções na tabela Visualiza
INSERT INTO Visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm) VALUES (1, 1, 1, 1, 1);
INSERT INTO Visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm) VALUES (2, 2, 2, 2, 2);

-- Inserções na tabela Laboratorio
INSERT INTO Laboratorio (status, id_reserva, id_chamado, id_usuario) VALUES ('Disponível', 1, 1, 1);
INSERT INTO Laboratorio (status, id_reserva, id_chamado, id_usuario) VALUES ('Ocupado', 2, 2, 2);

-- Inserções na tabela Chamado
INSERT INTO Chamado (status, id_lab, usado_equi, observacao, id_usuario) VALUES ('Aberto', 1, 'Projetor', 'Necessita de manutenção', 1);
INSERT INTO Chamado (status, id_lab, usado_equi, observacao, id_usuario) VALUES ('Fechado', 2, 'Computador', 'Resolvido', 2);

-- Inserções na tabela Agendamento
INSERT INTO Agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab) VALUES ('2024-08-20', '10:00:00', 20, 'Reunião mensal', 1, 1);
INSERT INTO Agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab) VALUES ('2024-08-21', '14:00:00', 15, 'Curso de extensão', 2, 2);

-- Inserções na tabela Abre_chamado
INSERT INTO Abre_chamado (id_docente, id_lab) VALUES (1, 1);
INSERT INTO Abre_chamado (id_docente, id_lab) VALUES (2, 2);

-- Inserções na tabela Gerencia
INSERT INTO Gerencia (id_tecnico, id_lab) VALUES (1, 1);
INSERT INTO Gerencia (id_tecnico, id_lab) VALUES (2, 2);

--Inserindo 4 entradas fixas para as rooms 
INSERT INTO room(id_room, horario, id_usuario) VALUES (1,'00:00:00', NULL),
INSERT INTO room(id_room, horario, id_usuario) VALUES (2,'00:00:00', NULL),
INSERT INTO room(id_room, horario, id_usuario) VALUES (3,'00:00:00', NULL),
INSERT INTO room(id_room, horario, id_usuario) VALUES (4,'00:00:00', NULL),


