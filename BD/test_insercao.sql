-- Visualizar dados na tabela Usuario
SELECT * FROM Usuario;

-- Visualizar dados na tabela Docente
SELECT * FROM Docente;

-- Visualizar dados na tabela Tecnico
SELECT * FROM Tecnico;

-- Visualizar dados na tabela Discente
SELECT * FROM Discente;

-- Visualizar dados na tabela Administrativo
SELECT * FROM Administrativo;

-- Visualizar dados na tabela Salas
SELECT * FROM Salas;

-- Visualizar dados na tabela Agenda
SELECT * FROM Agenda;

-- Visualizar dados na tabela Horarios
SELECT * FROM Horarios;

-- Visualizar dados na tabela Visualiza
SELECT * FROM Visualiza;

-- Visualizar dados na tabela Laboratorio
SELECT * FROM Laboratorio;

-- Visualizar dados na tabela Chamado
SELECT * FROM Chamado;

-- Visualizar dados na tabela Agendamento
SELECT * FROM Agendamento;

-- Visualizar dados na tabela Abre_chamado
SELECT * FROM Abre_chamado;

-- Visualizar dados na tabela Gerencia
SELECT * FROM Gerencia;

-- Visualizar usando uma agregação de tabelas 
SELECT 'Docente' AS tipo_usuario, COUNT(id_docente) AS total
FROM Docente
UNION ALL
SELECT 'Técnico' AS tipo_usuario, COUNT(id_tecnico) AS total
FROM Tecnico
UNION ALL
SELECT 'Discente' AS tipo_usuario, COUNT(id_discente) AS total
FROM Discente
UNION ALL
SELECT 'Administrativo' AS tipo_usuario, COUNT(id_adm) AS total
FROM Administrativo;


-- Visualizar usando uma busca inteligente(index) do nome

SELECT id_usuario, nome, matricula
FROM Usuario
WHERE nome = 'João Silva';

SELECT id_usuario, nome, matricula
FROM Usuario
WHERE nome = 'Maria Oliveira';
