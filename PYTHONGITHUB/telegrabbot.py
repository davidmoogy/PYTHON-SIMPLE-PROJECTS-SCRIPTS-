from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 'your_telegram_bot_token'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

main()
