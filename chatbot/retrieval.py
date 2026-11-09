
import os
import re
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# URL JSON dari GitHub
KNOWLEDGE_BASE_URL = os.getenv("KNOWLEDGE_BASE_URL")


def preprocess(text):
    """Membersihkan teks pertanyaan."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def load_knowledge_base():
    """Mengambil Knowledge Base berbentuk JSON dari GitHub."""

    if not KNOWLEDGE_BASE_URL:
        raise ValueError("KNOWLEDGE_BASE_URL belum diatur di file .env")

    response = requests.get(KNOWLEDGE_BASE_URL, timeout=15)
    response.raise_for_status()

    data = response.json()

    # Mendukung JSON dengan pembungkus knowledge_base
    if "knowledge_base" in data:
        data = data["knowledge_base"]

    return data


def search_knowledge_base(user_input):
    """Mencari jawaban yang paling sesuai."""

    knowledge_base = load_knowledge_base()
    question = preprocess(user_input)

    patterns = []
    intents = []

    # Mengumpulkan semua pola pertanyaan
    for intent, data in knowledge_base.items():
        for pattern in data.get("patterns", []):
            patterns.append(preprocess(pattern))
            intents.append(intent)

    if not patterns:
        return None

    # Periksa kecocokan langsung terlebih dahulu
    for intent, data in knowledge_base.items():
        for pattern in data.get("patterns", []):
            clean_pattern = preprocess(pattern)

            if clean_pattern and clean_pattern in question:
                responses = data.get("responses", [])
                if responses:
                    import random
                    return random.choice(responses)

    # Menggunakan TF-IDF dan Cosine Similarity
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(patterns + [question])

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    ).flatten()

    best_index = similarity.argmax()
    best_score = similarity[best_index]

    # Batas minimal kemiripan
    if best_score < 0.25:
        return None

    best_intent = intents[best_index]
    responses = knowledge_base[best_intent].get("responses", [])

    if not responses:
        return None

    import random
    return random.choice(responses)
