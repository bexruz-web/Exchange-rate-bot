from telegram import Update
from telegram.ext import ContextTypes
from get_exchange import send_exchange_rate

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    if 'Valyuta' in message:
        await send_exchange_rate(update, context)
    elif 'Dasturchi' in message:
        await update.message.reply_text("Bu botning dasturchisi: Bexruz Asqarov\nTelegram: @Web_BekxruzMe\nLoyihalar: @WikiSearchh_bot, @ob_havolar_haftalikbot")
    else:
        await update.message.reply_text("<Valyuta kursi> tugmasini bosing ")






