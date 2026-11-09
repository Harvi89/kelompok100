
const chatMessages = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-btn");
const newChatButton = document.getElementById("new-chat");
const typingIndicator = document.getElementById("typing-indicator");

// Menampilkan pesan ke area chat
function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}`;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = sender === "user" ? "K" : "AI";

    const content = document.createElement("div");
    content.className = "message-content";
    content.textContent = text;

    message.appendChild(avatar);
    message.appendChild(content);

    chatMessages.appendChild(message);

    // Otomatis scroll ke pesan terbaru
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Mengirim pertanyaan ke backend Python
async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) return;

    // Tampilkan pesan pengguna
    addMessage(message, "user");

    userInput.value = "";
    sendButton.disabled = true;

    if (typingIndicator) {
        typingIndicator.style.display = "block";
    }

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Gagal menghubungi server.");
        }

        const data = await response.json();

        // Tampilkan jawaban chatbot
        addMessage(
            data.response || "Maaf, chatbot belum memberikan jawaban.",
            "bot"
        );

    } catch (error) {
        console.error("Error:", error);

        addMessage(
            "Maaf, terjadi kesalahan. Pastikan server Python sedang berjalan.",
            "bot"
        );

    } finally {
        sendButton.disabled = false;

        if (typingIndicator) {
            typingIndicator.style.display = "none";
        }

        userInput.focus();
    }
}

// Klik tombol kirim
sendButton.addEventListener("click", sendMessage);

// Tekan Enter untuk mengirim pesan
userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

// Tombol percakapan baru
if (newChatButton) {
    newChatButton.addEventListener("click", function() {
        chatMessages.innerHTML = "";

        addMessage(
            "Halo! Saya Chatbot Jadwal Kuliah Informatika. Ada yang bisa saya bantu?",
            "bot"
        );
    });
}
