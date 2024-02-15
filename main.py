import telebot
import random

# Conexión con nuestro BOT
TU_TOKEN_AQUÍ = "6555420059:AAFQg0eWhHq0CbJ8NYSj1WQE9_CQpkzneao"
bot = telebot.TeleBot(TU_TOKEN_AQUÍ)

# Excusas
who = [
    "Pennywise",
    "El Jinete sin Cabeza",
    "Un selenita",
    "Un ser venido de otro planeta",
    "Godzilla",
    "Drácula",
    "Cthulhu"
  ];
action = [
    "comió",
    "destruyó",
    "quemó",
    "desintegró",
    "pulverizó",
    "escondió",
    "partió"
  ];
what = [
    "las llaves de mi casa",
    "el tejado del vecino",
    "mi coche nuevo",
    "las gafas de mi abuela",
    "los apuntes de HTML",
    "el monopatín de mi hermano pequeño"
  ];
when = [
    "después del almuerzo",
    "justo a tiempo",
    "después del concierto",
    "durante el viaje de fin de curso",
    "depués de las clases",
    "durante la misa del domingo",
    "durante la proyección de la película"
  ];




# Creación de los comandos básicos 
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenido a mi primer proyecto de bot de Telegram.
    
    Puedes usar los siguientes comandos conmigo:
    
    /start - Inicia una conversación conmigo
    /help - Obtiene ayuda sobre cómo usar el bot
    /about - Muestra información sobre este bot
    /excusa - Elabora una excusa convincente
    /clear - Limpia la pantalla
    
    ¡Espero que disfrutes usando este bot!
    """
    bot.reply_to(message, start_text)


@bot.message_handler(commands=['help']) 
def send_help(message):
    bot.reply_to(message, "¡Claro! Estoy aquí para ayudarte. Si tienes alguna pregunta o necesitas asistencia, no dudes en decírmelo. Estoy aquí para hacer que tu experiencia con este bot sea lo más fácil y agradable posible.")


@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    ¡Hola! Soy un bot de Telegram creado por EduardoHernandezGuzman para ayudarte en tus tareas diarias.
    
    Este bot fue creado como parte de mi primer proyecto de desarrollo de un bot de Telegram.
    """
    bot.reply_to(message, about_text)

@bot.message_handler(commands=['excusa'])
def send_random_excuse(message):
    random_who = random.choice(who)
    random_action = random.choice(action)
    random_what = random.choice(what)
    random_when = random.choice(when)
    random_excuse = f"{random_who} {random_action} {random_what} {random_when}."
    bot.reply_to(message, random_excuse)

@bot.message_handler(commands=['clear'])
def clear_screen(message):
    bot.delete_message(message.chat.id, message.message_id)




if __name__ == "__main__":
    bot.polling(none_stop=True)
