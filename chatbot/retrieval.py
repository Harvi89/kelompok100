import os
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Mengambil URL Knowledge Base dari .env
KB_URL = os.getenv("KNOWLEDGE_BASE_URL")

DIRECT_THRESHOLD = 0.55
MIN_RELEVANCE = 0.10
TOP_K = 3


def load_knowledge_base():

    if not KB_URL:
        raise ValueError("URL Knowledge Base belum diatur.")

    response = requests.get(
        KB_URL,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Format Knowledge Base harus berupa list JSON.")

    return data


# Membaca data dari GitHub
knowledge_base = load_knowledge_base()


def build_search_engine():

    documents = []

    for item in knowledge_base:

        text = (
            item["title"] + " " +
            item["content"] + " " +
            item["keywords"]
        )

        documents.append(text)

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        sublinear_tf=True
    )

    matrix = vectorizer.fit_transform(documents)

    return vectorizer, matrix


vectorizer, tfidf_matrix = build_search_engine()


def search_documents(question):

    question_vector = vectorizer.transform([question])

    scores = cosine_similarity(
        question_vector,
        tfidf_matrix
    )[0]

    ranked_indices = scores.argsort()[::-1]

    results = []

    for index in ranked_indices[:TOP_K]:

        results.append({
            "document": knowledge_base[index],
            "score": float(scores[index])
        })

    return results


def retrieve(question):

    results = search_documents(question)

    if not results:
        return {
            "mode": "unknown",
            "context": [],
            "score": 0
        }

    best = results[0]
    best_score = best["score"]

    if (
        best_score >= DIRECT_THRESHOLD
        and best["document"]["direct_answer"]
    ):

        return {
            "mode": "direct",
            "answer": best["document"]["direct_answer"],
            "context": [best],
            "score": best_score
        }

    if best_score < MIN_RELEVANCE:

        return {
            "mode": "unknown",
            "context": [],
            "score": best_score
        }

    return {
        "mode": "llm",
        "context": results,
        "score": best_score
    }