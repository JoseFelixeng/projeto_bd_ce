document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#registration-form');
    const errorMessage = document.querySelector('#error-message');

    form.addEventListener('submit', async function (event) {
        event.preventDefault(); // Evita o envio padrão do formulário

        const email = document.querySelector('#email').value;
        const senha = document.querySelector('#password').value;
        const tipo = document.querySelector('#tipo').value;

        if (!email || !senha || !tipo) {
            errorMessage.textContent = "Todos os campos são obrigatórios!";
            return;
        }

        // Criptografar a senha usando bcrypt
        const hashedSenha = await bcrypt.hash(senha, 10); // Salta a criptografia, no front-end geralmente não é recomendada

        // Enviar dados para o backend
        try {
            const response = await fetch('http://localhost:8000/cadastro/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: email,
                    senha: hashedSenha,
                    tipo: parseInt(tipo, 10)
                })
            });

            if (response.ok) {
                // Cadastro bem-sucedido, redireciona para a página de login ou outra
                window.location.href = 'login.html';
            } else {
                const errorData = await response.json();
                errorMessage.textContent = errorData.detail || "Erro ao cadastrar usuário.";
            }
        } catch (error) {
            console.error('Erro:', error);
            errorMessage.textContent = "Erro na comunicação com o servidor.";
        }
    });
});
