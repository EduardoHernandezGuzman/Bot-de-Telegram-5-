import telebot
import random
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde la variable de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Lista de caracteres para generar la contraseña
caracteres = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "!", "@", "#", "$", "%", "&", "*", "+", "-"
]

# CREACION DE LOS COMANDOS BASICOS

#Comando /start
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenid@ a mis primeros proyectos de bots de Telegram.
    
    Puedes usar los siguientes comandos conmigo:
    
    /start - Inicia una conversación conmigo
    /about - Muestra información sobre este bot
    /password - Elabora una contraseña aleatoria
    
    ¡Espero que disfrutes usando este bot!
    """
    bot.reply_to(message, start_text)


#Comando /about
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    ¡Hola! Soy un bot de Telegram creado por EduardoHernandezGuzman para ayudarte a generar una contraseña aleatoria.
    
    Este bot fue creado como parte de mis primeros proyectos de desarrollo de bots de Telegram.
    """
    bot.reply_to(message, about_text)


# Comando /contraseña
@bot.message_handler(commands=['password'])
def contraseña(message):
    valor = 9

    nueva_contraseña = ''.join(random.choice(caracteres) for _ in range(valor))
    bot.reply_to(message, f"Tu nueva contraseña es: {nueva_contraseña}")


if __name__ == "__main__":
    bot.polling(none_stop=True)