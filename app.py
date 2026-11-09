
from flask import Flask, render_template, request, jsonify

from chatbot.retrieval import search_knowledge_base
from chatbot.llm import ask_openai

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({
                "response": "Silakan masukkan pertanyaan terlebih dahulu."
            }), 400

        # Tahap 1: Cari jawaban di Knowledge Base
        answer = search_knowledge_base(user_message)

        if answer:
            return jsonify({
                "response": answer,
                "source": "knowledge_base"
            })

        # Tahap 2: Jika tidak ditemukan, gunakan OpenAI
        answer = ask_openai(user_message)

        return jsonify({
            "response": answer,
            "source": "openai"
        })

    except Exception as error:
        print("Terjadi kesalahan:", error)

        return jsonify({
            "response": (
                "Maaf, terjadi kesalahan pada chatbot. "
                "Silakan coba kembali."
            )
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
