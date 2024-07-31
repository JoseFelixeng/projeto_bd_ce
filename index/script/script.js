document.getElementById('cadastroForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const matricula = document.getElementById('matricula').value;
    const senha = document.getElementById('senha').value;
    const email = document.getElementById('email').value;
    const tipo = document.getElementById('tipo').value;

    const usuario = {
        nome: nome,
        matricula: parseInt(matricula),
        senha: senha, // Envie a senha em texto simples
        email: email,
        tipo: parseInt(tipo)
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/cadastro/', { // Corrigido o endpoint para /cadastro/
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(usuario)
        });

        if (response.ok) {
            const result = await response.json();
            alert('Usuário cadastrado com sucesso!');
        } else {
            const error = await response.json();
            alert('Erro ao cadastrar usuário: ' + error.detail);
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao cadastrar usuário.');
    }
});

function togglePassword() {
    const passwordField = document.getElementById('senha');
    const passwordFieldType = passwordField.getAttribute('type');
    if (passwordFieldType === 'password') {
        passwordField.setAttribute('type', 'text');
    } else {
        passwordField.setAttribute('type', 'password');
    }
}
