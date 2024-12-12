import aiohttp
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
from config import API_URL

async def get_exchange_rate():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

async def send_exchange_rate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = await get_exchange_rate()
    if data:
        usd = next((item for item in data if item['Ccy'] == "USD"), {})
        eur = next((item for item  in data if item['Ccy'] == "EUR"), {})
        rub = next((item for item  in data if item['Ccy'] == "RUB"), {})

        message = (
            f"{datetime.today().strftime('%Y-%m-%d')} dagi valyuta kursi:\n\n"
            f"<b>AQSH dollari:</b>\n💵 1 {usd.get('Ccy')} = {usd.get('Rate')} UZS\n📊 {usd.get('Diff')} UZS\n\n"
            f"<b>EVRO:</b>\n💶 1 {eur.get('Ccy')} = {eur.get('Rate')} UZS\n📊 {eur.get('Diff')} UZS\n\n"
            f"<b>Rossiya rubli:</b>\n💴 1 {rub.get('Ccy')} = {rub.get('Rate')} UZS\n📊 {rub.get('Diff')} UZS\n\n"
            f"Ps: Barcha malumotlar <b>Markaziy Bank</b> rasmiy saytidan olindi: https://cbu.uz"

        )
    else:
        message = "Malumot olishda xatolik yuz berdi. Qayta urining..."
    await update.message.reply_text(message, parse_mode='HTML')
