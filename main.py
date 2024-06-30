import telebot
import random
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde la variable de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

#Lista de excusas
who = [
    "Pennywise",
    "El Jinete sin Cabeza",
    "Un selenita",
    "Un ser venido de otro planeta",
    "Godzilla",
    "Drácula",
    "Cthulhu",
    "El Hombre Lobo",
    "El Yeti",
    "La Momia",
    "El Fantasma de la Ópera",
    "La Bruja",
    "El Monstruo del Lago Ness",
    "El Hombre Invisible",
    "El Alienígena",
    "La Criatura del Pantano",
    "El Vampiro",
    "El Demonio",
    "El Zombi"
]

action = [
    "comió",
    "destruyó",
    "quemó",
    "desintegró",
    "pulverizó",
    "escondió",
    "partió",
    "trituró",
    "devoró",
    "aplastó",
    "rompió",
    "hundió",
    "robo",
    "consumió",
    "abdujo",
    "derritió",
    "borró",
    "contaminó",
    "envenenó"
]

what = [
    "las llaves de mi casa",
    "el tejado del vecino",
    "mi coche nuevo",
    "las gafas de mi abuela",
    "los apuntes de HTML",
    "el monopatín de mi hermano pequeño",
    "el teléfono móvil",
    "el ordenador portátil",
    "el control remoto de la televisión",
    "la carta de amor",
    "el pastel de cumpleaños",
    "el libro de hechizos",
    "la lámpara mágica",
    "el trofeo del torneo",
    "la joya del museo",
    "la fórmula secreta",
    "el mapa del tesoro",
    "la varita mágica",
    "la poción de la juventud"
]

when = [
    "después del almuerzo",
    "justo a tiempo",
    "después del concierto",
    "durante el viaje de fin de curso",
    "después de las clases",
    "durante la misa del domingo",
    "durante la proyección de la película",
    "en plena noche",
    "al amanecer",
    "en pleno día",
    "en la hora de la siesta",
    "durante la cena",
    "en la hora punta",
    "durante la tormenta",
    "en la luna llena",
    "en pleno eclipse",
    "en el momento más inesperado",
    "en el peor momento posible",
    "justo antes de la boda"
]

# CREACION DE LOS COMANDOS BASICOS

#Comando /start
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenido a uno de mis primeros bots de Telegram.
    
    Puedes usar los siguientes comandos conmigo:
    
    /start - Inicia una conversación conmigo
    /about - Muestra información sobre este bot
    /excusa - Elabora una excusa convincente
    
    ¡Espero que disfrutes usando este bot!
    """
    bot.reply_to(message, start_text)


#Comando /about
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    ¡Hola! Soy un bot de Telegram creado por EduardoHernandezGuzman para ayudarte en tus tareas diarias.
    
    Este bot fue creado como parte de mi primer proyecto de desarrollo de un bot de Telegram.
    """
    bot.reply_to(message, about_text)

#Comando /excusa
@bot.message_handler(commands=['excusa'])
def send_random_excuse(message):
    random_who = random.choice(who)
    random_action = random.choice(action)
    random_what = random.choice(what)
    random_when = random.choice(when)
    random_excuse = f"{random_who} {random_action} {random_what} {random_when}."
    bot.reply_to(message, random_excuse)



if __name__ == "__main__":
    bot.polling(none_stop=True)