import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN") or "rom telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
TOKEN = "9208514850:AAEkVvsVHa0F-DuCiRh7TDEue_aaExWlMvE"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 THE MODZ BOT ACTIVO 🔥")
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Iniciando...")
app.run_polling()"
MI_ID = 123456789 # Tu ID de admin, opcional

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 THE MODZ BOTZ 🔥", callback_data="menu")],
        [InlineKeyboardButton("✅ Comandos", callback_data="comandos")]
    ]
    await update.message.reply_text("¡Bienvenido a THE MODZ BOTZ!", reply_markup=InlineKeyboardMarkup(keyboard))

async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "menu":
        await query.edit_message_text("🔥 THE MODZ BOTZ - Nivel 5 Activado 🔥")
    elif query.data == "comandos":
        await query.edit_message_text("/start - Iniciar\n/help - Ayuda")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botones))

print("BOT INICIADO 24/7...")
app.run_polling()
