import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 LOS MODZ BOTZ 🔥", callback_data="menu")],
        [InlineKeyboardButton("✅ Comandos", callback_data="comandos")]
    ]
    await update.message.reply_text("🔥 EL MODZ BOT ACTIVO 🔥", reply_markup=InlineKeyboardMarkup(keyboard))

async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "menu":
        await query.edit_message_text("🔥 THE MODZ BOTZ - Nivel 5 Activado 🔥")
    elif query.data == "comandos":
        await query.edit_message_text("/start - Iniciar\n/help - Ayuda")

logging.basicConfig(level=logging.INFO)
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botones))
print("BOT INICIADO 24/7...")
app.run_polling()
