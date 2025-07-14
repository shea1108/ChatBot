 const inputBox = document.getElementById("input-box");
    const sendButton = document.getElementById("send-button");
    const chatWindow = document.getElementById("chat-window");

    function appendMessage(content, type) {
      const msg = document.createElement("div");
      msg.classList.add("message", type);
      msg.textContent = content;
      chatWindow.appendChild(msg);
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    async function sendMessage() {
      const text = inputBox.value.trim();
      if (!text) return;

      appendMessage(text, "user");
      inputBox.value = "";

      try {
        const response = await fetch("/chat/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ question: text })
        });

        const result = await response.json();
        if (response.ok) {
          appendMessage(result.answer, "bot");
        } else {
          appendMessage("⚠️ Lỗi: " + result.error, "bot");
        }
      } catch (error) {
        appendMessage("⚠️ Không thể kết nối server.", "bot");
      }
    }

    sendButton.addEventListener("click", sendMessage);
    inputBox.addEventListener("keydown", (e) => {
      if (e.key === "Enter") sendMessage();
    });