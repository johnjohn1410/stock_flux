function sendMessage() {
    const userInput = document.getElementById('user-input');
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
            debugger;
            appendMessage('bot', data.response || 'Desculpe, não consegui entender.');
        })
        .catch(error => {
            console.error('Erro:', error);
            appendMessage('bot', 'Ocorreu um erro. Tente novamente mais tarde.');
        });
    }
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
