  import os
  from telegram import Update
  from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

  BOT_TOKEN = os.getenv("BOT_TOKEN")
  GROUP_CHAT_ID = int(os.getenv("GROUP_CHAT_ID"))

  async def forward_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
      if update.message:
          await update.message.forward(chat_id=GROUP_CHAT_ID)

  app = ApplicationBuilder().token(BOT_TOKEN).build()
  app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), forward_to_group))

  app.run_polling()
