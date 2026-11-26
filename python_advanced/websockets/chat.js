// The WebSocket server address
const wsUri = "ws://localhost:8000/ws";
const websocket = new WebSocket(wsUri);
//"As soon as you create this object, it will start trying to connect"

// Get the status element from the page
const statusEl = document.getElementById("status");

// When the connection opens, show "connected"
websocket.addEventListener("open", () => {
  statusEl.textContent = "متصل ✅";
});

// Get the messages area from the page
const messagesEl = document.getElementById("messages");

// When a message arrives, add it to the page
websocket.addEventListener("message", (e) => {
  const line = document.createElement("p");
  line.textContent = "السيرفر: " + e.data;
  messagesEl.appendChild(line);
});

// Get the input and the button from the page
const inputEl = document.getElementById("msgInput");
const sendBtn = document.getElementById("sendBtn");

// When the button is clicked, send the message
sendBtn.addEventListener("click", () => {
  const text = inputEl.value;

  if (text.trim() === "") {
    return;
  }

  websocket.send(text);

  const line = document.createElement("p");
  line.textContent = "أنت: " + text;
  messagesEl.appendChild(line);

  inputEl.value = "";
});

websocket.addEventListener("close", () =>{
    statusEl.textContent = "Closed";
});
