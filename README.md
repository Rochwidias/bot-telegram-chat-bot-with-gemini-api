readme_content = """# BotRen - Telegram Gemini AI Bot 🤖

**BotRen** adalah Telegram Bot berbasis Python yang memanfaatkan **Google Gemini AI API** untuk memberikan respon otomatis yang cepat, cerdas, dan interaktif. Bot ini dilengkapi dengan fitur pengolahan pesan teks secara *streaming*, kemampuan menganalisis/membaca gambar, proteksi *anti-spam*, serta sistem *logging* internal.

---

## 🌟 Fitur Utama

- 🧠 **Integrasi Google Gemini AI**: Menggunakan model Gemini AI untuk menjawab pertanyaan teks maupun menganalisis gambar.
- ⚡ **Streaming Text Response**: Efek teks yang mengetik secara *real-time* saat AI menghasilkan jawaban.
- 🖼️ **Analisis Gambar (Vision/Multimodal)**: Mampu membaca dan menjelaskan gambar yang dikirimkan oleh pengguna.
- 🛡️ **Anti-Spam & Cooldown**: Fitur pembatas jeda waktu (5 detik) untuk mencegah penggunaan berlebihan (*rate-limit*).
- 📝 **Logging Otomatis**: Menyimpan semua riwayat percakapan dan status sistem ke dalam file `chat_log.txt`.
- 🔁 **Auto Reconnect / Auto Restart**: Menggunakan *loop* otomatis jika terjadi kendala jaringan atau *crash*.

---

## 🛠️ Prasyarat & Teknologi

Sebelum menjalankan bot ini, pastikan Anda telah menyiapkan:

* **Python 3.9+**
* **Bot Token Telegram** (dapat dibuat melalui [@BotFather](https://t.me/BotFather))
* **API Key Google Gemini** (dapat diperoleh melalui [Google AI Studio](https://aistudio.google.com/))

### Library Python
- `python-telegram-bot`
- `google-generativeai`

---

## 🚀 Cara Instalasi & Penggunaan

### 1. Clone Repository
```bash
git clone [https://github.com/Rochwidias/bot-telegram-chat-bot-with-gemini-api](https://github.com/Rochwidias/bot-telegram-chat-bot-with-gemini-api)
cd BotJawir# bot-telegram-chat-bot-with-gemini-api
