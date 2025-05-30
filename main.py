# Importar las bibliotecas necesarias
import discord  # Biblioteca para trabajar con la API de Discord
from discord.ext import commands  # Controlar el bot basado en comandos
import requests  # Biblioteca para hacer solicitudes HTTP
import pyttsx3  # Biblioteca para la síntesis de voz
# Inicializar los intents del bot (permisos)
intents = discord.Intents.default()  # Crea los intents por defecto
intents.message_content = True  # Permite al bot leer los mensajes
# Crear el bot con el prefijo "!" y los intents configurados
bot = commands.Bot(command_prefix="!", intents=intents)
# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()  # Crea un objeto para la síntesis de voz
# Ejecutar el bot (reemplaza 'TU_TOKEN_AQUI' con el token real del bot)


def get_fact() -> str:
    """
    Recupera un dato curioso aleatorio desde la API.
    Retorna:
        str: El texto del dato o un mensaje de error.
    """
    base_url = "https://uselessfacts.jsph.pl/random.json?language=es"
    response = requests.get(base_url)
    data = response.json()
    print(data)  # Para depuración
    # Verifica que el idioma sea español
    if response.status_code == 200:
        return data.get("text", "No se pudo obtener el dato.")
    else:
        return "No se pudo obtener un dato en español. Intenta de nuevo."


def speak(text: str):
    """
    Vocaliza el texto proporcionado usando pyttsx3.
    Parámetros:
        text (str): Texto que se va a vocalizar
    """
    engine.say(text)  # Añade el texto a la  síntesis de voz
    engine.runAndWait()  # Procesa y vocaliza el texto


@bot.command()  # Define un comando llamado "start" para el bot
async def start(ctx):
    """
    Comando para dar la bienvenida al usuario.
    Parámetros:
        ctx: Contexto del comando (información sobre la invocación del comando)
    """
    mensaje = "Soy tu bot de datos curiosos. Usa !fact para recibir un hecho interesante."
    await ctx.send(mensaje)  # Envía mensaje de bienvenida a Discord


@bot.command()  # Define un comando llamado "fact" para el bot
async def fact(ctx):
    """
    Comando para recuperar un dato curioso aleatorio y vocalizarlo.
    Parámetros:
        ctx: Contexto del comando (información sobre la invocación del comando)
    """
    random_fact = get_fact()  # Obtiene un dato curioso aleatorio
    await ctx.send(f"Aquí tienes un dato curioso: {random_fact}")  # Envía el dato al canal de Discord
    speak(random_fact)  # Vocaliza el dato usando pyttsx3


bot.run("TOKEN")  # Inicia el bot y lo conecta a Discord
