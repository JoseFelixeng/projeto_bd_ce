-- Buscar todos os usuários
SELECT * FROM Usuario;

-- Buscar todos os docentes
SELECT * FROM Docente;

-- Buscar todos os técnicos
SELECT * FROM Tecnico;

-- Buscar todos os discentes
SELECT * FROM Discente;

-- Buscar todos os administrativos
SELECT * FROM Administrativo;

-- Buscar todas as salas
SELECT * FROM Salas;

-- Buscar todas as agendas
SELECT * FROM Agenda;

-- Buscar todos os horários
SELECT * FROM Horarios;

-- Buscar todas as visualizações
SELECT * FROM Visualiza;

-- Buscar todos os laboratórios
SELECT * FROM Laboratorio;

-- Buscar todos os chamados
SELECT * FROM Chamado;

-- Buscar todos os agendamentos
SELECT * FROM Agendamento;

-- Buscar todos os chamados abertos pelos docentes
SELECT * FROM Abre_chamado;

-- Buscar todas as gerências de laboratórios por técnicos
SELECT * FROM Gerencia;


-- Buscar detalhes do docente Maria Souza, incluindo informações do usuário
SELECT d.*, u.nome, u.matricula, u.senha 
FROM Docente d
JOIN Usuario u ON d.id_usuario = u.id_usuario
WHERE d.nome = 'Maria Souza';
