from telegram.ext import ApplicationBuilder, CommandHandler,ConversationHandler, CallbackQueryHandler, MessageHandler, filters
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from transacciones import Retiro,Recarga
from models import User
import db

retiro = Retiro()
recarga = Recarga()

async def start(update, context):
    user = update.message.from_user
    if not db.session.query(User).filter_by(userTelegramId=user.id).first():
        new_user = User(userTelegramId=user.id,username=user.username,name=user.first_name)
        db.session.add(new_user)
        db.session.commit()
        
    keyboard = [
        [InlineKeyboardButton("Account",callback_data="account")],
        [InlineKeyboardButton("\U00002795 Recargar", callback_data="recargar"),InlineKeyboardButton("\U00002796 Retirar",callback_data="retirar")],
        [InlineKeyboardButton("\U0001F6CD Mercado", callback_data="mercado"),InlineKeyboardButton("\U0001F9D1\U0000200D\U0001F33E My Land",callback_data="granero")],
        [InlineKeyboardButton("\U0001F465 Referidos", callback_data="referidos"),InlineKeyboardButton("\U0001F4B8 Historial",callback_data="historial")],
    ]
    
    markup =  InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text="Menu principal de la Granja. Aqui puedes comprar animales e ir generando ingresos por ellos",reply_markup=markup)

async def account(query):
    userTelegram = query.from_user
    user = db.session.query(User).filter_by(userTelegramId=userTelegram.id)
    await query.edit_message_text(f"Name: {user.name}\nUserName: {user.username}\nID: {user.userTelegramId}\nBalance: CUP\n\nYou can buy properties in marketplace to earn money every hour.")
    return ConversationHandler.END
    
async def myland(update,context,query):
    userTelegram = query.from_user
    user = db.session.query(User).filter_by(userTelegramId=userTelegram.id)
    await query.edit_message_text("No se puede mostrar esta informacion todavia.")
    return ConversationHandler.END

async def button(update,context):
    query = update.callback_query
    data = query.data
    
    if data == "account":
        return await account(update,context,query)
    if data == "myland":
        return await myland(update,context,query)
    if data == "recargar":
        return await recarga.preguntar_cantidad(query)
    if data == "retirar":
        return await retiro.preguntar_cantidad(query)

def main():           
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
    
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    main()
