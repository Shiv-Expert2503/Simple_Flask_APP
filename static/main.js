document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("chat-form");
    const messages = document.getElementById("chat-messages");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
      const userMessage = document.getElementById("user-message").value;
      appendMessage("You", userMessage);
      sendMessage(userMessage);
      document.getElementById("user-message").value = "";
    });
  
    function appendMessage(sender, message) {
      const messageElement = document.createElement("div");
      messageElement.classList.add("message");
      messageElement.innerHTML = `<strong>${sender}: </strong>${message}`;
      messages.appendChild(messageElement);
    }
  
    function sendMessage(userInput) {
      fetch("/chatbot", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify({
          user_input: userInput
        })
      })
        .then(response => response.json())
        .then(data => {
          const botResponse = data.bot_response;
          appendMessage("ChatBot", botResponse);
        })
        .catch(error => console.error("Error:", error));      
    }
  });
  