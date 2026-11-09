knowledge_base = {
    "greeting": {
        "patterns": [
            "halo",
            "hai",
            "hello",
            "selamat pagi",
            "selamat siang",
            "selamat sore",
            "selamat malam",
            "permisi"
        ],
        "responses": [
            "Halo! Selamat datang di Chatbot Jadwal Kuliah Informatika. Ada yang bisa saya bantu?",
            "Hai! Saya siap membantu memberikan informasi seputar perkuliahan Informatika."
        ]
    },

    "jadwal_kuliah": {
        "patterns": [
            "jadwal kuliah",
            "jadwal kelas",
            "kapan kuliah",
            "jadwal perkuliahan",
            "jadwal informatika",
            "jadwal mahasiswa",
            "mata kuliah hari ini",
            "jadwal minggu ini",
            "jam kuliah"
        ],
        "responses": [
            "Saya dapat membantu mencari informasi jadwal kuliah. Silakan sebutkan nama mata kuliah atau hari yang ingin kamu cari."
        ]
    },

    "mata_kuliah": {
        "patterns": [
            "daftar mata kuliah",
            "mata kuliah informatika",
            "apa saja mata kuliah",
            "nama mata kuliah",
            "informasi mata kuliah",
            "mata kuliah semester ini"
        ],
        "responses": [
            "Saya dapat membantu memberikan informasi mata kuliah Informatika. Sebutkan nama mata kuliah yang ingin kamu ketahui."
        ]
    },

    "dosen": {
        "patterns": [
            "nama dosen",
            "siapa dosen",
            "dosen pengampu",
            "pengajar mata kuliah",
            "dosen informatika",
            "siapa yang mengajar"
        ],
        "responses": [
            "Saya dapat membantu mencari informasi dosen pengampu. Sebutkan nama mata kuliahnya."
        ]
    },

    "ruangan": {
        "patterns": [
            "ruangan kuliah",
            "lokasi kelas",
            "dimana kelas",
            "nomor ruangan",
            "ruang perkuliahan",
            "tempat kuliah"
        ],
        "responses": [
            "Saya dapat membantu mencari informasi ruangan kuliah. Sebutkan nama mata kuliah yang ingin kamu cari."
        ]
    },

    "lokasi_kampus": {
        "patterns": [
            "lokasi kampus",
            "alamat kampus",
            "dimana kampus",
            "letak kampus",
            "lokasi universitas"
        ],
        "responses": [
            "Informasi lokasi kampus dapat diperoleh melalui website resmi atau bagian administrasi kampus."
        ]
    },

    "kontak_admin": {
        "patterns": [
            "kontak admin",
            "hubungi admin",
            "nomor admin",
            "email admin",
            "kontak akademik",
            "bagian akademik"
        ],
        "responses": [
            "Untuk informasi lebih lanjut mengenai jadwal kuliah, silakan hubungi bagian akademik kampus."
        ]
    },

    "terima_kasih": {
        "patterns": [
            "terima kasih",
            "makasih",
            "thanks",
            "terima kasih banyak",
            "sangat membantu"
        ],
        "responses": [
            "Sama-sama! Senang bisa membantu.",
            "Dengan senang hati! Semoga perkuliahanmu lancar."
        ]
    },

    "goodbye": {
        "patterns": [
            "bye",
            "sampai jumpa",
            "selamat tinggal",
            "keluar",
            "exit"
        ],
        "responses": [
            "Sampai jumpa! Semoga harimu menyenangkan.",
            "Terima kasih sudah menggunakan Chatbot Jadwal Kuliah Informatika!"
        ]
    }
}

FALLBACK_RESPONSE = (
    "Maaf, saya belum memahami pertanyaan Anda. "
    "Silakan tanyakan seputar jadwal kuliah Informatika."
)

