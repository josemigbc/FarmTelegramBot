from telegram.ext import ApplicationBuilder, CommandHandler,ConversationHandler, CallbackQueryHandler, MessageHandler, filters
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from transacciones import Retiro,Recarga

retiro = Retiro()
recarga = Recarga()

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Actualizar","https://t.me/JoseMiguelCF")],
        [InlineKeyboardButton("\U00002795 Recargar", callback_data="recargar"),InlineKeyboardButton("\U00002796 Retirar",callback_data="retirar")],
        [InlineKeyboardButton("\U0001F6CD Mercado", callback_data="mercado"),InlineKeyboardButton("\U0001F9D1\U0000200D\U0001F33E Granero",callback_data="granero")],
        [InlineKeyboardButton("\U0001F42E Animales", callback_data="animales"),InlineKeyboardButton("\U0001F4B8 Historial",callback_data="historial")],
        [InlineKeyboardButton("\U0001F465 Referidos", callback_data="referidos"),InlineKeyboardButton("\U00002699 Ajustes",callback_data="ajustes")],
        [InlineKeyboardButton("\U00002753 FAQ", callback_data="faq"),InlineKeyboardButton("\U0001F4AC Chat",callback_data="chat")],
    ]
    
    markup =  InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text="Menu principal de la Granja. Aqui puedes comprar animales e ir generando ingresos por ellos",reply_markup=markup)

async def button(update,context):
    query = update.callback_query
    data = query.data
    
    if data == "recargar":
        return await recarga.preguntar_cantidad(query)
    if data == "retirar":
        return await retiro.preguntar_cantidad(query)
            
# App core
TOKEN = "1733325599:AAHz1mPy1hJv_jnEFK89Ifyqd3J0uio8MNE"

# Create app
app = ApplicationBuilder().token(TOKEN).build()

# Add the commands
app.add_handler(CommandHandler("start", start))

app.add_handler(
    ConversationHandler(
        entry_points=[CallbackQueryHandler(button)],
        states={
            recarga.AMOUNT: [MessageHandler(filters.TEXT,recarga.mensaje_confirmacion)],
            retiro.AMOUNT: [MessageHandler(filters.TEXT,retiro.mensaje_confirmacion)],
        },
        fallbacks=[],
    )
)

# start bot
app.run_polling()
