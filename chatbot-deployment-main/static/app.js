document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const messagesHistory = document.querySelector('.messages__history');

    // Function to scroll to the bottom of the chat
    function scrollToBottom() {
        const chatbox = document.querySelector('.chatbox__messages');
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function addMessage(message, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.className = isUser ? 'messages__item messages__item--operator' : 'messages__item messages__item--visitor';
        messageDiv.textContent = message;
        messagesHistory.appendChild(messageDiv);
        scrollToBottom();
    }

    async function sendMessage() {
        const message = messageInput.value.trim();
        if (message === '') return;

        // Clear input and add user message
        messageInput.value = '';
        addMessage(message, true);

        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Server error');
            }

            // Add bot response with a small delay
            setTimeout(() => {
                if (data.error) {
                    addMessage('Sorry, I encountered an error. Please try again.', false);
                } else {
                    addMessage(data.answer, false);
                }
            }, 500);

        } catch (error) {
            console.error('Error:', error);
            setTimeout(() => {
                addMessage('Sorry, I encountered a network error. Please check your connection and try again.', false);
            }, 500);
        }
    }

    // Add click event listener to send button
    sendButton.addEventListener('click', sendMessage);

    // Add enter key event listener to input field
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Focus input field on load
    messageInput.focus();
});