-- Inserções na tabela Usuario
INSERT INTO Usuario (nome, matricula, senha) VALUES ('Ana Silva', 123477878, 'senha123');
INSERT INTO Usuario (nome, matricula, senha) VALUES('Eduardo', 987367581,'12345');
INSERT INTO Usuario (nome, matricula, senha) VALUES('Carlos Souza', 3456789012, 's545498');
INSERT INTO Usuario (nome, matricula, senha) VALUES('patricia', 34567892, 's54549348');
INSERT INTO Usuario (nome, matricula, senha) VALUES('José Felix', 1234567890, 's54549348');
INSERT INTO Usuario (nome, matricula, senha) VALUES('João Mendes', 4567890123, '9876324132');

-- Criando um index em nome
CREATE INDEX i ON Usuario (nome);

SHOW INDEX FROM Usuario;

SELECT * FROM usuario;

-- Atualizações nas tabelas
UPDATE usuario SET nome = 'José Felix Atualizado' WHERE id_usuario = 5;

SELECT * FROM usuario;

-- Inserções na tabela Docente
INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario) VALUES ('Dr. Pedro Santos', 1001, 'Matemática', 'Ciências Exatas', 1);
INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario) VALUES ('Dra. Ana Costa', 1002, 'Física', 'Ciências Exatas', 2);

SELECT * FROM Docente;


-- Inserções na tabela Tecnico
INSERT INTO Tecnico (nome, matricula, id_usuario) VALUES ('Carlos Pereira', 2001, 1);
INSERT INTO Tecnico (nome, matricula, id_usuario) VALUES ('Fernanda Lima', 2002, 2);

SELECT * FROM Tecnico;

-- Inserções na tabela Discente
INSERT INTO Discente (nome, matricula, id_usuario) VALUES ('Lucas Almeida', 3001, 1);
INSERT INTO Discente (nome, matricula, id_usuario) VALUES ('Juliana Santos', 3002, 2);

SELECT * FROM Discente;

-- Inserções na tabela Administrativo
INSERT INTO Administrativo (nome, matricula, id_usuario) VALUES ('Ana Paula', 4001, 1);
INSERT INTO Administrativo (nome, matricula, id_usuario) VALUES ('Bruno Martins', 4002, 2);

SELECT * FROM Administrativo;

-- Inserções na tabela Salas
INSERT INTO Salas (sala, laboratorio, auditorio) VALUES (101, 'Lab A', 'Auditório 1');
INSERT INTO Salas (sala, laboratorio, auditorio) VALUES (102, 'Lab B', 'Auditório 2');

SELECT * FROM Salas;

-- Inserções na tabela Agenda
INSERT INTO Agenda (nome, disciplina, turma, quant_alunos) VALUES ('Matemática I', 'Matemática', 'Turma A', 30);
INSERT INTO Agenda (nome, disciplina, turma, quant_alunos) VALUES ('Física I', 'Física', 'Turma B', 25);

SELECT * FROM Agenda;

-- Inserções na tabela Horarios
INSERT INTO Horarios (id_usuario, id_agenda, id_sala) VALUES (1, 1, 1);
INSERT INTO Horarios (id_usuario, id_agenda, id_sala) VALUES (2, 2, 2);

SELECT * FROM Horarios;

-- Inserções na tabela Visualiza
INSERT INTO Visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm) VALUES (1, 1, 1, 1, 1);
INSERT INTO Visualiza (id_docente, id_discente, id_tecnico, id_horarios, id_adm) VALUES (2, 2, 2, 2, 2);

SELECT * FROM Visualiza;

-- Deleções nas tabelas
DELETE FROM Visualiza WHERE id_horarios = 1;

SELECT * FROM Visualiza;

-- Inserções na tabela Laboratorio
INSERT INTO Laboratorio (status, id_reserva, id_chamado, id_usuario) VALUES ('Disponível', 1, 1, 1);
INSERT INTO Laboratorio (status, id_reserva, id_chamado, id_usuario) VALUES ('Ocupado', 2, 2, 2);

SELECT * FROM Laboratorio;

UPDATE Laboratorio SET status = 'Em manutenção' WHERE id_lab = 1;

SELECT * FROM laboratorio;

-- Inserções na tabela Chamado
INSERT INTO Chamado (status, id_lab, usado_equi, observacao, id_usuario) VALUES ('Aberto', 1, 'Projetor', 'Necessita de manutenção', 1);
INSERT INTO Chamado (status, id_lab, usado_equi, observacao, id_usuario) VALUES ('Fechado', 2, 'Computador', 'Resolvido', 2);

SELECT * FROM Chamado;

UPDATE Chamado SET status = 'Concluido' WHERE id_chamado = 1;

SELECT * FROM Chamado;


-- Inserções na tabela Agendamento
INSERT INTO Agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab) VALUES ('2024-08-20', '10:00:00', 20, 'Reunião mensal', 1, 1);
INSERT INTO Agendamento (data, horario, quant_alunos, observacao, id_usuario, id_lab) VALUES ('2024-08-21', '14:00:00', 15, 'Curso de extensão', 2, 2);

SELECT * FROM Agendamento;

-- Inserções na tabela Abre_chamado
INSERT INTO Abre_chamado (id_docente, id_lab) VALUES (1, 1);
INSERT INTO Abre_chamado (id_docente, id_lab) VALUES (2, 2);

SELECT * FROM Abre_chamado;

-- Inserções na tabela Gerencia
INSERT INTO Gerencia (id_tecnico, id_lab) VALUES (1, 1);
INSERT INTO Gerencia (id_tecnico, id_lab) VALUES (2, 2);

SELECT * FROM Gerencia;

-- Deleções nas tabelas
DELETE FROM Gerencia WHERE id_tecnico = 1 AND id_lab = 1;
SELECT * FROM Gerencia;

--Inserindo 4 entradas fixas para as rooms 
INSERT INTO room(id_room, horario, id_usuario) VALUES (1,'10:00:00', 1);
INSERT INTO room(id_room, horario, id_usuario) VALUES (2,'13:00:00', 2);
INSERT INTO room(id_room, horario, id_usuario) VALUES (3,'17:00:00', 2);
INSERT INTO room(id_room, horario, id_usuario) VALUES (4,'20:00:00', 1);

SELECT * FROM room;

-- Deleções nas tabelas
DELETE FROM room WHERE id_room = 1;

SELECT * FROM room;


-- Criando uma Busca por professor, sala e horario
SELECT 
    d.nome AS docente_nome,
    h.id_horarios AS horario_id,
    h.id_agenda AS agenda_id,
    s.sala AS sala_numero
FROM 
    Docente d
JOIN 
    Horarios h ON d.id_usuario = h.id_usuario
JOIN 
    Salas s ON h.id_sala = s.id_sala;


