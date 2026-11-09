from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from chatbot.retrieval import retrieve_documents
from chatbot.llm import ask_openai, UNKNOWN_ANSWER

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

        # Tahap 1: Cari informasi di Knowledge Base
        result = retrieve_documents(user_message)

        # Tahap 2: Jika skor tinggi, jawab langsung dari KB
        if result["mode"] == "direct":
            return jsonify({
                "response": result["answer"],
                "source": "knowledge_base",
                "score": round(result["score"], 3)
            })

        # Tahap 3: Jika skor rendah, kirim Top-K konteks ke LLM
        if result["mode"] == "context":
            answer = ask_openai(
                user_message,
                result["contexts"]
            )

            return jsonify({
                "response": answer,
                "source": "llm_with_context",
                "score": round(result["score"], 3)
            })

        # Tahap 4: Jika tidak ada konteks yang relevan
        return jsonify({
            "response": UNKNOWN_ANSWER,
            "source": "no_context"
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
