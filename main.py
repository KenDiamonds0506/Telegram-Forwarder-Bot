from flask import Flask, request
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

SOURCE_CHAT_ID = -1002536057440  # ID group
TARGET_USER_ID = 7165721191      # ID người nhận

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]

        if chat_id == SOURCE_CHAT_ID:
            message_id = message["message_id"]
            try:
                bot.forward_message(
                    chat_id=TARGET_USER_ID,
                    from_chat_id=chat_id,
                    message_id=message_id
                )
            except Exception as e:
                print("Forward error:", e)

    return "OK"

@app.route('/')
def index():
    return 'Bot is alive!'
