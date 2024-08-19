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

-- Mostrar todas as tabelas e suas colunas
SELECT TABLE_NAME, COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'projetoBD';

-- Exibir a contagem de registros em cada tabela
SELECT 
    TABLE_NAME, 
    TABLE_ROWS 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'projetoBD';

-- Exibir todos os dados de todas as tabelas (executar individualmente conforme necessário)
SELECT * FROM Usuario;
SELECT * FROM Docente;
SELECT * FROM Tecnico;
SELECT * FROM Discente;
SELECT * FROM Administrativo;
SELECT * FROM Salas;
SELECT * FROM Agenda;
SELECT * FROM Horarios;
SELECT * FROM Visualiza;
SELECT * FROM Laboratorio;
SELECT * FROM Chamado;
SELECT * FROM Agendamento;
SELECT * FROM Abre_chamado;
SELECT * FROM Gerencia;
