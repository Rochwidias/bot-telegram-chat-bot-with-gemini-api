import os
import time
import asyncio
import traceback
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import google.generativeai as genai # Library Gemini

# --- KONFIGURASI ---
TOKEN = ''
GEMINI_API_KEY = ''

# Inisialisasi Gemini
genai.configure(api_key=GEMINI_API_KEY)

model_name = 'gemini-3.5-flash'

SYSTEM_PROMPT = """Kamu adalah BotJawir, asisten AI cerdas buatan @Rochwidias.
Patuhi aturan berikut saat merespons:
1. Selalu awali setiap jawabanmu dengan persis kalimat ini: "BotJawir buatan @Rochwidias di sini: "
2. Jika pertanyaan tidak jelas, jawab dengan sopan bahwa kamu tidak mengerti.
3. respons menggunakan emoji yang ramah dan bahasa yang santai ajah kayak anak gen z.
4. respons harus medium lah tidak banyak tidak kurang agar user memahami jawaban yang kamu berikan kepada user.
5. JANGAN PERNAH menggunakan tanda bintang (*) untuk bold atau list. Gunakan teks biasa saja.
6. respon dengan efisien.
7. respon dengan efisien namun kompleks."""

# Konfigurasi Model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1000,
}

# Inisialisasi model dengan System Instruction
gemini_model = genai.GenerativeModel(
    model_name=model_name,
    generation_config=generation_config,
    system_instruction=SYSTEM_PROMPT
)

# --- PENGATURAN ANTI-SPAM ---
COOLDOWN_TIME = 5 
user_cooldowns = {} 

def simpan_log(pengirim, tipe, pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text = f"[{waktu}] {pengirim} | {tipe}: {pesan}\n"
    print(log_text.strip())
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(log_text)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    error_msg = f"Exception saat memproses update:\n{traceback.format_exc()}"
    simpan_log("SYSTEM", "CRITICAL ERROR", error_msg)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return

    chat_id = update.effective_chat.id
    user = update.effective_user
    user_id = user.id
    username = f"@{user.username}" if user.username else user.first_name
    
    # --- ANTI-SPAM LOGIC ---
    current_time = time.time()
    if user_id in user_cooldowns:
        time_passed = current_time - user_cooldowns[user_id]
        if time_passed < COOLDOWN_TIME:
            simpan_log(username, "SYSTEM (SPAM BLOCKED)", "Pesan diabaikan karena cooldown.")
            return 
        
    user_cooldowns[user_id] = current_time

    await context.bot.send_chat_action(chat_id=chat_id, action="typing")
    
    # --- PENANGANAN GAMBAR ---
    if update.message.photo:
        prompt = update.message.caption if update.message.caption else "Jelaskan gambar ini."
        simpan_log(username, "USER (GAMBAR)", prompt)
        
        try:
            # Ambil file gambar
            photo_file = await update.message.photo[-1].get_file()
            image_bytes = await photo_file.download_as_bytearray()
            
            # Format untuk Gemini
            image_parts = [
                {"mime_type": "image/jpeg", "data": bytes(image_bytes)}
            ]
            
            # Generate response
            response = gemini_model.generate_content([prompt] + image_parts)
            jawaban_bot = response.text.replace("*", "") # Hapus tanda bintang jika AI bandel
            
            simpan_log("BotJawir", "BOT (BALASAN GAMBAR)", jawaban_bot)
            await context.bot.send_message(chat_id=chat_id, text=jawaban_bot)
            
        except Exception as e:
            simpan_log("SYSTEM", "ERROR GAMBAR", str(e))
            await context.bot.send_message(chat_id=chat_id, text="BotJawir buatan @Rochwidias di sini: Aduh, gagal baca gambarnya nih bro. 😅")

    # --- PENANGANAN TEKS (STREAMING) ---
    elif update.message.text:
        user_text = update.message.text
        simpan_log(username, "USER (TEKS)", user_text)
        
        sent_message = await context.bot.send_message(chat_id=chat_id, text="Sabar bos lagi mikir.. 😎")
        full_reply = ""
        
        try:
            # Request streaming ke Gemini
            response = gemini_model.generate_content(user_text, stream=True)
            
            last_edit_time = time.time()
            for chunk in response:
                full_reply += chunk.text
                full_reply = full_reply.replace("*", "") # Hapus tanda bintang sesuai request
                
                # Update pesan setiap 2 detik agar tidak kena rate limit Telegram
                if time.time() - last_edit_time > 2.0:
                    try:
                        await context.bot.edit_message_text(
                            chat_id=chat_id, 
                            message_id=sent_message.message_id, 
                            text=full_reply + "..."
                        )
                        last_edit_time = time.time()
                    except:
                        pass
            
            # Final update
            await context.bot.edit_message_text(
                chat_id=chat_id, 
                message_id=sent_message.message_id, 
                text=full_reply
            )
            simpan_log("BotJawir", "BOT (BALASAN TEKS)", full_reply)
            
        except Exception as e:
            error_msg = f"Error Gemini: {e}"
            simpan_log("SYSTEM", "ERROR", error_msg)
            await context.bot.edit_message_text(
                chat_id=chat_id, 
                message_id=sent_message.message_id, 
                text="BotJawir buatan @Rochwidias di sini: Lagi ada gangguan koneksi ke otak AI-ku nih. 😅"
            )

def main():
    while True:
        try:
            print("\n========================================")
            print("BotJawir GEMINI AI aktif...")
            print("========================================\n")
            
            application = ApplicationBuilder().token(TOKEN).build()
            application.add_handler(MessageHandler(filters.PHOTO | filters.TEXT & (~filters.COMMAND), handle_message))
            application.add_error_handler(error_handler)
            
            application.run_polling(drop_pending_updates=True)
            
        except Exception as e:
            print(f"Bot Crash: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()