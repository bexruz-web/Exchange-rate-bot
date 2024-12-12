from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import BOT_TOKEN
from message import message_handler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["💱 Valyuta kursi"], ["👨‍💻 Dasturchi"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(f"Salom👋🏻 <b>{update.effective_user.first_name}</b>\nValyuta kurslarini aniq ko'rsatadigan botga Xush Kelibsiz!!! "
                                    f"Kursni ko'rish uchun <b>Valyuta kursi</b> tugmasini bosing", reply_markup=reply_markup, parse_mode="HTML")

def main() -> None:
    print('Bot Started...')
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()

if __name__ == '__main__':
    main()

