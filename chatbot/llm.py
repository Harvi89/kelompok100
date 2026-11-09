
import os
from openai import OpenAI


def ask_openai(question):
    """Mengirim pertanyaan ke model OpenAI."""

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "API Key OpenAI belum diatur."

    client = OpenAI(api_key=api_key)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    response = client.responses.create(
        model=model,
        instructions=(
            "Kamu adalah asisten akademik untuk mahasiswa "
            "Informatika. Jawab menggunakan bahasa Indonesia "
            "yang jelas, sopan, dan mudah dipahami. "
            "Jangan mengarang jadwal, nama dosen, atau ruangan. "
            "Jika data spesifik tidak tersedia, katakan dengan jujur."
        ),
        input=question
    )

    return response.output_text
