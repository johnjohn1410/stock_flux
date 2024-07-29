function entrar() {
    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;
    // Adicione aqui a lógica de autenticação
    if (login && senha) {
        window.location.href = 'pagina_principal.html'; // redireciona para a página principal
    } else {
        alert('Por favor, preencha todos os campos.');
    }
}