-- teste de inserções

INSERT INTO Usuario (nome, matricula, senha, id_docente, id_tecnico, id_discente) VALUES 
('João Silva', 123456, 'senha123', NULL, NULL, NULL),
('Maria Souza', 789012, 'outrasenha456', NULL, NULL, NULL),
('José Pereira', 13579, 'senha789', NULL, NULL, NULL),
('Pedro Fernandes', 24680, 'senha456', NULL, NULL, NULL),
('Ana Lima', 11223, 'senha321', NULL, NULL, NULL);


INSERT INTO Docente (nome, matricula, disciplina, departamento, id_usuario) VALUES 
('Prof. Carlos Oliveira', 98765, 'Matemática', 'Ciências Exatas', 1), -- id_usuario 1 corresponde a João Silva
('Prof. Ana Santos', 54321, 'Física', 'Ciências Naturais', 2); -- id_usuario 2 corresponde a Maria Souza


INSERT INTO Tecnico (nome, matricula, id_usuario) VALUES 
('José Pereira', 13579, 3); -- id_usuario 3 corresponde a José Pereira


INSERT INTO Discente (nome, matricula, id_usuario) VALUES 
('Pedro Fernandes', 24680, 4); -- id_usuario 4 corresponde a Pedro Fernandes



INSERT INTO Administrativo (nome, matricula, id_usuario) VALUES 
('Ana Lima', 11223, 5); -- id_usuario 5 corresponde a Ana Lima
