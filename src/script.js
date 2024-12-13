document.getElementById("send-button").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    
    if (userInput.trim() !== "") {
        // Display user message
        displayMessage(userInput, "user");
        
        // Clear input field
        document.getElementById("user-input").value = "";

        // Simulate chatbot response (in reality, this will be replaced with a backend API call)
        simulateBotResponse(userInput);
    }
});

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    
    messageElement.classList.add(sender === "user" ? "user-message" : "bot-message");
    messageElement.textContent = message;
    
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function simulateBotResponse(userMessage) {
    let botMessage = "";

    // Example response logic (based on the user's input)
    if (userMessage.toLowerCase().includes("recommend")) {
        botMessage = "Based on your profile, I recommend the following courses: \n1. Introduction to AI\n2. Machine Learning for Beginners\n3. Deep Learning Specialization";
    } else if (userMessage.toLowerCase().includes("hello")) {
        botMessage = "Hello! How can I assist you with your career today?";
    } else {
        botMessage = "I didn't quite understand that. Can you please clarify?";
    }

    // Display bot response after a delay
    setTimeout(function() {
        displayMessage(botMessage, "bot");
    }, 1000);
}
