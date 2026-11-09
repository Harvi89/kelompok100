import json
import re
import random
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Pengaturan pencarian
DIRECT_THRESHOLD = 0.45
MIN_CONTEXT_SCORE = 0.10
TOP_K = 3

# Lokasi folder data
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Empat file Knowledge Base
KB_FILES = [
    "kb_jadwal.json",
    "kb_akademik.json",
    "kb_kemahasiswaan.json",
    "kb_informasi_kampus.json"
]


def preprocess(text):
    """Membersihkan teks sebelum proses pencarian."""
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_knowledge_base():
    """Memuat seluruh Knowledge Base dari empat file JSON."""

    all_documents = []

    for filename in KB_FILES:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"File Knowledge Base tidak ditemukan: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Mendukung pembungkus knowledge_base
        if isinstance(data, dict) and "knowledge_base" in data:
            data = data["knowledge_base"]

        # Format JSON berupa list
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    continue

                responses = item.get("responses", [])
                answer = item.get("answer", "")

                if not answer and responses:
                    answer = random.choice(responses)

                all_documents.append({
                    "id": item.get("id", ""),
                    "category": item.get("category", ""),
                    "content": item.get("content", ""),
                    "patterns": item.get("patterns", []),
                    "answer": answer
                })

        # Mendukung format JSON lama berupa dictionary
        elif isinstance(data, dict):
            for intent, item in data.items():
                if not isinstance(item, dict):
                    continue

                responses = item.get("responses", [])
                answer = item.get("answer", "")

                if not answer and responses:
                    answer = random.choice(responses)

                all_documents.append({
                    "id": intent,
                    "category": intent,
                    "content": item.get("content", answer),
                    "patterns": item.get("patterns", []),
                    "answer": answer
                })

    return all_documents


def retrieve_documents(user_question):
    """
    Mencari dokumen menggunakan TF-IDF dan Cosine Similarity.

    Mode:
    - direct: jawaban langsung dari Knowledge Base.
    - context: mengirim Top-K konteks ke LLM.
    - none: tidak ditemukan konteks relevan.
    """

    documents = load_knowledge_base()

    question = preprocess(user_question)

    if not question or not documents:
        return {
            "mode": "none",
            "answer": None,
            "contexts": []
        }

    searchable_texts = []

    for document in documents:
        patterns = document.get("patterns", [])

        if not isinstance(patterns, list):
            patterns = []

        searchable = " ".join([
            str(document.get("content", "")),
            str(document.get("answer", "")),
            str(document.get("category", "")),
            *[str(pattern) for pattern in patterns]
        ])

        searchable_texts.append(preprocess(searchable))

    try:
        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(
            searchable_texts + [question]
        )

        similarities = cosine_similarity(
            vectors[-1],
            vectors[:-1]
        ).flatten()

    except ValueError:
        return {
            "mode": "none",
            "answer": None,
            "contexts": []
        }

    # Mengurutkan dokumen berdasarkan skor tertinggi
    ranked_indices = similarities.argsort()[::-1]

    best_index = int(ranked_indices[0])
    best_score = float(similarities[best_index])

    # Tahap 1: Jawaban langsung jika skor tinggi
    if best_score >= DIRECT_THRESHOLD:
        answer = documents[best_index].get("answer")

        if answer:
            return {
                "mode": "direct",
                "answer": answer,
                "score": best_score,
                "contexts": []
            }

    # Tahap 2: Ambil Top-K konteks jika skor rendah
    contexts = []

    for index in ranked_indices[:TOP_K]:
        score = float(similarities[index])

        if score < MIN_CONTEXT_SCORE:
            continue

        document = documents[int(index)]

        contexts.append({
            "id": document.get("id"),
            "category": document.get("category"),
            "content": document.get("content"),
            "answer": document.get("answer"),
            "score": score
        })

    # Tahap 3: Tidak ada konteks yang relevan
    if not contexts:
        return {
            "mode": "none",
            "answer": None,
            "contexts": []
        }

    return {
        "mode": "context",
        "answer": None,
        "score": best_score,
        "contexts": contexts
    }
