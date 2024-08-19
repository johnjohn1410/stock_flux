function sendMessage(userInput) {
    const message = userInput.value.trim();

    if (message) {
        appendMessage('user', message);
        userInput.value = '';

        fetch('http://localhost:5000/api/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'accept': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('bot', data.response || 'Desculpe, não consegui entender.');
        })
        .catch(error => {
            console.error('Erro:', error);
            appendMessage('bot', 'Ocorreu um erro. Tente novamente mais tarde.');
        });
    }
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-content');
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', sender);
    messageElement.textContent = message;
    const messageRow = document.createElement('div');
    messageRow.appendChild(messageElement);
    messageRow.classList.add('row', sender);
    chatBox.appendChild(messageRow);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function toggleChat() {
    var chatBody = document.getElementById("chat-body");
    var toggleIcon = document.getElementById("toggle-icon");

    if (chatBody.style.display === "none" || chatBody.style.display === "") {
        chatBody.style.display = "block";
        toggleIcon.textContent = "−";  // Ícone de minimizar
    } else {
        chatBody.style.display = "none";
        toggleIcon.textContent = "+";  // Ícone de maximizar
    }
}

// Adicionar event listener para o botão de envio
document.getElementById("send-button").addEventListener("click", function() {
    var userInput = document.getElementById("chat-input");
    sendMessage(userInput);
    document.getElementById("chat-input").value = ""; // Limpar o campo de entrada
});


const userInput = document.getElementById("chat-input");
document.getElementById("send-button").addEventListener("click", function() {
    sendMessage(userInput);
    userInput.value = "";
});
userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage(userInput);
        userInput.value = "";
    }
});

