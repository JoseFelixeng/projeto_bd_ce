USE projetoBD;

-- Inserção na tabela Usuario
INSERT INTO Usuario (nome, matricula, senha)
VALUES 
('João Silva', 12345, 'senha123'),
('Maria Souza', 67890, 'senha456'),
('Pedro Lima', 54321, 'senha789'),
('Ana Paula', 11223, 'senha001');

-- Inserção na tabela Docente
INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario)
VALUES 
('Maria Souza', 67890, 'Matemática', 'Exatas', 2);

-- Inserção na tabela Tecnico
INSERT INTO Tecnico (nome, matricula, id_usuario)
VALUES 
('João Silva', 12345, 1);

-- Inserção na tabela Discente
INSERT INTO Discente (nome, matricula, id_usuario)
VALUES 
('Pedro Lima', 54321, 3);

-- Inserção na tabela Administrativo
INSERT INTO Administrativo (nome, matricula, id_usuario)
VALUES 
('Ana Paula', 11223, 4);

-- Inserção na tabela Salas
INSERT INTO Salas (sala, laboratorio, auditorio)
VALUES 
(101, 'Lab de Informática', NULL),
(102, NULL, 'Auditorio Principal');

-- Inserção na tabela Agenda
INSERT INTO Agenda (nome, disciplina, turma, quant_alunos)
VALUES 
('Aula de Matemática', 'Matemática', 'Turma A', 30),
('Aula de Física', 'Física', 'Turma B', 25);

-- Inserção na tabela Horarios
INSERT INTO Horarios (id_usuario, id_agenda, id_sala)
VALUES 
(2, 1, 1),
(3, 2, 2);

-- Inserção na tabela Visualiza
INSERT INTO Visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm)
VALUES 
(1, NULL, 1, 1, NULL),
(NULL, 1, NULL, 2, NULL);

-- Inserção na tabela Laboratorio
INSERT INTO Laboratorio (status)
VALUES 
('Disponível'),
('Em uso');

-- Inserção na tabela Chamado
INSERT INTO Chamado (status, id_lab, usado_equi, observacao, id_usuario)
VALUES 
('Aberto', 1, 'Projetor', 'Problema no projetor', 1),
('Fechado', 2, 'Computador', 'Computador reiniciando sozinho', 2);

-- Inserção na tabela Agendamento
INSERT INTO Agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab)
VALUES 
('2024-08-14', '10:00:00', 25, 'Aula prática', 2, 1);

-- Inserção na tabela Abre_chamado
INSERT INTO Abre_chamado (id_docente, id_lab)
VALUES 
(1, 1);

-- Inserção na tabela Gerencia
INSERT INTO Gerencia (id_tecnico, id_lab)
VALUES 
(1, 1);
