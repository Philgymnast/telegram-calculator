from telegram.ext import Updater, CommandHandler

TOKEN = "8277238553:AAEBdUfMoumt8BK_A_0-tZ5yXITYaKc-PwA"


def start(update, context):
    update.message.reply_text("Привет! Я бот. Пиши /help")

def help_command(update, context):
    update.message.reply_text("Команды: /start, /help")

def main():

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    print("✅ Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()