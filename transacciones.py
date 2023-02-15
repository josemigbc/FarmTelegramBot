from telegram.ext import ConversationHandler

class Transaccion():
    
    AMOUNT = 0
    type = ""
    
    async def preguntar_cantidad(self,query,text):
        await query.edit_message_text(text)
        return self.AMOUNT
    
    async def mensaje_confirmacion(self,update,context):
        if update.message.text.isnumeric():
            await update.message.reply_text(f"Haz hecho una solicitud de {self.type} exitosamente de {update.message.text} CUP. Por favor espera a que sea confirmada por un administrador.")
            return ConversationHandler.END
        await update.message.reply_text("Debes introducir un numero...")
        return self.AMOUNT

class Retiro(Transaccion):
    
    AMOUNT = 1
    type = "retiro"
    
    async def preguntar_cantidad(self, query):
        text = "Introduce el monto que deseas retirar y espera la confirmacion de un administrador."
        return await super().preguntar_cantidad(query, text)
    
class Recarga(Transaccion):
    
    AMOUNT = type = "recarga"
    
    async def preguntar_cantidad(self, query):
        text = "Envia el monto con el que deseas recargar tu cuenta a 9205 XXXX XXXX XXXX y espera la confirmacion de la recarga."
        return await super().preguntar_cantidad(query, text)      