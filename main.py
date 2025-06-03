import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = int(os.getenv("GROUP_CHAT_ID"))

# Fake Flask server để Render không kill bot
web_app = Flask(__name__)

@web_app.route('/')
def index():
    return "✅ Telegram bot is running!"

def run_web():
    web_app.run(host='0.0.0.0', port=10000)

# Bot handler
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.forward(chat_id=GROUP_CHAT_ID)

# Start bot
def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_message))
    app.run_polling()

# Chạy song song: Flask + Telegram Bot
if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    run_bot()
