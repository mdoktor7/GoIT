document.addEventListener("DOMContentLoaded", () => {
  const formChat = document.getElementById("formChat");
  const textField = document.getElementById("textField");
  const subscribeDiv = document.getElementById("subscribe");

  const ws = new WebSocket("ws://localhost:9090");

  ws.onopen = () => {
    console.log("Connected to the WebSocket server");
  };

  ws.onmessage = (event) => {
    const message = document.createElement("div");
    message.textContent = event.data;
    subscribeDiv.appendChild(message);
  };

  ws.onerror = (error) => {
    console.error("WebSocket error:", error);
  };

  ws.onclose = () => {
    console.log("Disconnected from the WebSocket server");
  };

  formChat.addEventListener("submit", (event) => {
    event.preventDefault();
    const message = textField.value;
    if (message) {
      ws.send(message);
      textField.value = "";
    }
  });
});
