# BotJawir - Telegram Gemini AI Bot 🤖

BotJawir adalah Telegram Bot berbasis Python yang memanfaatkan Google Gemini AI API untuk memberikan respon otomatis yang cepat, cerdas, dan interaktif. Bot ini dilengkapi dengan fitur pengolahan pesan teks secara streaming, kemampuan menganalisis/membaca gambar, proteksi anti-spam, serta sistem logging internal.

---

## 🌟 Fitur Utama

- 🧠 Integrasi Google Gemini AI: Menggunakan model Gemini AI untuk menjawab pertanyaan teks maupun menganalisis gambar.
- ⚡ Streaming Text Response: Efek teks yang mengetik secara real-time saat AI menghasilkan jawaban.
- 🖼️ Analisis Gambar (Vision/Multimodal): Mampu membaca dan menjelaskan gambar yang dikirimkan oleh pengguna.
- 🛡️ Anti-Spam & Cooldown: Fitur pembatas jeda waktu (5 detik) untuk mencegah penggunaan berlebihan (rate-limit).
- 📝 Logging Otomatis: Menyimpan semua riwayat percakapan dan status sistem ke dalam file chat_log.txt.
- 🔁 Auto Reconnect / Auto Restart: Menggunakan loop otomatis jika terjadi kendala jaringan atau crash.

---

## 🛠️ Prasyarat & Teknologi

Sebelum menjalankan bot ini, pastikan Anda telah menyiapkan:

* Python 3.9+
* Bot Token Telegram (dapat dibuat melalui @BotFather)
* API Key Google Gemini (dapat diperoleh melalui Google AI Studio)

### Library Python
- python-telegram-bot
- google-generativeai
- python-dotenv

---

## 🚀 Cara Instalasi & Penggunaan

### 1. Clone Repository
git clone https://github.com/Rochwidias/bot-telegram-chat-bot-with-gemini-api.git
cd bot-telegram-chat-bot-with-gemini-api

### 2. Install Dependensi
Jalankan perintah berikut untuk menginstal library yang dibutuhkan:
pip install python-telegram-bot google-generativeai python-dotenv

### 3. Konfigurasi Token & API Key
Buat file .env di folder utama project dan isi dengan kredensial Anda:

TELEGRAM_TOKEN=BOT_TOKEN_TELEGRAM_KAMU
GEMINI_API_KEY=GEMINI_API_KEY_KAMU

Catatan Keamanan: Jangan membagikan file .env atau API Key asli Anda secara publik ke GitHub! Gunakan .gitignore untuk menyembunyikannya.

### 4. Jalankan Bot
Eksekusi file Python untuk menjalankan bot:
python bot.py

---

## 📂 Struktur File

├── bot.py           # Script utama BotJawir
├── chat_log.txt     # File log otomatis (dibuat saat bot berjalan)
├── .env             # File variabel lingkungan (keamanan token)
├── .gitignore       # Menyaring file agar tidak masuk ke GitHub
└── README.txt       # Dokumentasi proyek (versi TXT)

---

## 👨‍💻 Pembuat

Dikembangkan oleh @Rochwidias.