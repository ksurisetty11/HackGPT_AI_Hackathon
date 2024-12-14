// Function to send the user input to the Flask backend and display the response
function sendMessage() {
    const userInput = document.getElementById('user-input').value;

    if (userInput.trim() !== "") {
        // Send the message to the /chat route
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "user_input": userInput })
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                document.getElementById('chat-output').innerHTML = data.response;
            } else {
                document.getElementById('chat-output').innerHTML = 'Sorry, I didn\'t get that!';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
