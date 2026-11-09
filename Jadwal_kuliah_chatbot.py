import re

knowledge_base = {
    "greeting": {
        "patterns": ["halo", "hai", "selamat pagi", "selamat siang"],
        "responses": [
            "Halo! Ada yang bisa saya bantu terkait informasi kampus?"
        ]
    },
    "jadwal_kuliah": {
        "patterns": ["jadwal kuliah", "jadwal kelas", "kapan kuliah"],
        "responses": [
            "Jadwal kuliah dapat dilihat di portal akademik pada menu 'Jadwal Kuliah'."
        ]
    },
    "lokasi_kampus": {
        "patterns": ["lokasi kampus", "alamat kampus", "dimana kampus"],
        "responses": [
            "Kampus berlokasi di Jl. Pendidikan No. 1, dekat halte busway terdekat."
        ]
    },
    "kontak_admin": {
        "patterns": ["kontak admin", "hubungi admin", "nomor admin"],
        "responses": [
            "Admin akademik dapat dihubungi di admin@kampus.ac.id atau (021) 555-0100."
        ]
    },
    "terima_kasih": {
        "patterns": ["terima kasih", "makasih", "thanks"],
        "responses": [
            "Sama-sama! Senang bisa membantu."
        ]
    },
    "goodbye": {
        "patterns": ["bye", "sampai jumpa", "keluar", "exit"],
        "responses": [
            "Sampai jumpa! Semoga harimu menyenangkan."
        ]
    }
}

FALLBACK_RESPONSE = "Maaf, saya belum memahami pertanyaan Anda. Bisa dijelaskan dengan kalimat lain?"

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def match_intent(user_input):
    processed = preprocess(user_input)

    for intent, data in knowledge_base.items():
        for pattern in data["patterns"]:
            if pattern in processed:
                return intent

    return None

import random

def generate_response(intent):
    if intent is none;
        return FALLBACK_RESPONSE
    responses = knowledge_base[intent]["responses"]     
    return random.choice(responses) 

def get_response(user_input):
     intent = match_intent(user_input)
     return generate_response(intent) 
