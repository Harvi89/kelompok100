Anggota Kelompok:
1. Harviansyah Siringo-ringo (25343013)
2. Christian Andrico Rajagukguk (25343008)
3. Hilman Fahmi (25343015)
4. Husnul Zidan (25343016)

# 🤖 Chatbot Akademik Informatika

Chatbot Akademik Informatika merupakan aplikasi chatbot berbasis Artificial Intelligence (AI) yang dirancang untuk membantu mahasiswa memperoleh informasi seputar kegiatan akademik dan lingkungan kampus.

Aplikasi ini menggunakan pendekatan **Retrieval-Augmented Generation (RAG)** dengan menggabungkan metode pencarian informasi TF-IDF dan Cosine Similarity serta Large Language Model (LLM) dari OpenAI.

Tujuan utama project ini adalah menghasilkan chatbot yang mampu memberikan jawaban berdasarkan informasi yang tersedia dalam Knowledge Base sehingga dapat mengurangi risiko jawaban yang tidak sesuai atau dibuat-buat.

---

## 📌 Fitur Utama

- **Chatbot Interaktif:** Pengguna dapat mengajukan pertanyaan menggunakan bahasa sehari-hari.
- **Knowledge Base:** Menyimpan informasi akademik dan kampus dalam format JSON.
- **TF-IDF:** Mengubah teks menjadi representasi numerik untuk proses pencarian.
- **Cosine Similarity:** Mengukur tingkat kemiripan antara pertanyaan pengguna dan informasi dalam Knowledge Base.
- **Top-K Retrieval:** Mengambil beberapa informasi paling relevan sebagai konteks untuk LLM.
- **Integrasi OpenAI API:** Menghasilkan jawaban berdasarkan konteks Knowledge Base.
- **Jawaban Berbasis Konteks:** Jika informasi tidak tersedia atau tidak mencukupi, chatbot diarahkan untuk menjawab bahwa informasi tidak diketahui.

## 🧠 Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Flask | Framework backend |
| HTML | Struktur halaman web |
| CSS | Tampilan antarmuka |
| JavaScript | Interaksi chatbot |
| Scikit-learn | Implementasi TF-IDF dan Cosine Similarity |
| OpenAI API | Large Language Model |
| JSON | Penyimpanan Knowledge Base |
| Git & GitHub | Pengelolaan versi dan kolaborasi |

## 📂 Struktur Project

```text
kelompok100/
│
├── app.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
│
├── chatbot/
│   ├── __init__.py
│   ├── retrieval.py
│   └── llm.py
│
├── data/
│   ├── kb_jadwal.json
│   ├── kb_akademik.json
│   ├── kb_kemahasiswaan.json
│   └── kb_informasi_kampus.json
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## 📚 Pembagian Knowledge Base

Knowledge Base dibagi menjadi empat kategori agar pengelolaan informasi dapat dilakukan oleh setiap anggota kelompok.

| File | Isi Informasi |
|---|---|
| `kb_jadwal.json` | Jadwal kuliah, mata kuliah, dosen, dan ruangan |
| `kb_akademik.json` | KRS, KHS, SKS, IPK, UTS, dan UAS |
| `kb_kemahasiswaan.json` | Beasiswa, organisasi, UKM, dan kegiatan mahasiswa |
| `kb_informasi_kampus.json` | Perpustakaan, Wi-Fi, laboratorium, dan fasilitas kampus |

Setiap data Knowledge Base menggunakan informasi berupa kategori, isi informasi, pola pertanyaan (*patterns*), dan jawaban (*answer*).

## ⚙️ Cara Instalasi dan Menjalankan Project

### 1. Clone Repository

Buka terminal atau PowerShell, kemudian jalankan:

```bash
git clone https://github.com/Harvi89/kelompok100.git
```

Masuk ke folder project:

```bash
cd kelompok100
```

### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

Aktifkan virtual environment pada Windows:

```powershell
venv\Scripts\Activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Mengatur Environment Variable

Buat file `.env` pada folder utama project.

Isi dengan konfigurasi berikut:

```env
OPENAI_API_KEY=masukkan_api_key_openai
OPENAI_MODEL=gpt-4.1-mini
```

Ganti `masukkan_api_key_openai` dengan API Key OpenAI milik sendiri.

**Penting:** Jangan membagikan API Key dan jangan mengunggah file `.env` ke GitHub.

### 5. Menjalankan Aplikasi

Jalankan perintah berikut:

```bash
python app.py
```

Jika berhasil, buka browser dan akses:

```text
http://127.0.0.1:5000
```

Chatbot dapat digunakan melalui halaman web tersebut.

## 🔄 Alur Kerja Chatbot

1. Pengguna memasukkan pertanyaan melalui antarmuka chatbot.
2. Backend Flask menerima pertanyaan.
3. Sistem melakukan pencarian informasi pada empat file Knowledge Base.
4. TF-IDF dan Cosine Similarity menghitung kemiripan pertanyaan dengan dokumen.
5. Jika skor kemiripan tinggi, chatbot memberikan jawaban langsung dari Knowledge Base.
6. Jika skor kemiripan lebih rendah, sistem mengambil Top-K dokumen paling relevan.
7. Konteks tersebut dikirim bersama pertanyaan pengguna ke OpenAI API.
8. LLM menyusun jawaban hanya berdasarkan konteks yang diberikan.
9. Jika informasi tidak cukup, chatbot diarahkan untuk memberikan jawaban tidak tahu.

## 🔐 Pembatasan Jawaban AI

Untuk mengurangi risiko halusinasi (*AI hallucination*), chatbot menggunakan instruksi sistem yang membatasi LLM agar hanya menggunakan informasi dari Knowledge Base.

Apabila informasi yang dibutuhkan tidak ditemukan atau tidak cukup dalam konteks, chatbot diarahkan untuk menjawab:

> Maaf, saya tidak tahu karena informasi tersebut tidak tersedia atau tidak cukup dalam Knowledge Base.

## 👥 Kolaborasi Tim

Project ini dikembangkan secara berkelompok menggunakan GitHub sebagai media kolaborasi dan pengelolaan kode program.

Setiap anggota dapat berkontribusi dengan mengembangkan bagian aplikasi maupun memperbarui Knowledge Base sesuai pembagian tugas.

## 🎯 Tujuan Project

Project ini dibuat sebagai implementasi pembelajaran mengenai:

- Pengembangan aplikasi berbasis AI.
- Penerapan Large Language Model.
- Implementasi Information Retrieval.
- Penggunaan TF-IDF dan Cosine Similarity.
- Integrasi Python dengan OpenAI API.
- Pengelolaan data menggunakan JSON.
- Kolaborasi pengembangan perangkat lunak menggunakan GitHub.

## 🔗 Repository

GitHub: https://github.com/Harvi89/kelompok100

---

**Chatbot Akademik Informatika**  
Dikembangkan sebagai project pembelajaran dan implementasi Artificial Intelligence pada bidang pendidikan.
