"""pyttsx3 examples."""

import pyttsx3
def configuracion(velocidad=125, volumen=1.0, voz=1):
    engine = pyttsx3.init()  # object creation

    # RATE
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty("rate", velocidad)  # setting up new voice rate


    # VOLUME
    volume = engine.getProperty("volume")  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty("volume", volumen)  # setting up volume level  between 0 and 1

    # VOICE
    voices = engine.getProperty("voices")  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
    engine.setProperty("voice", voices[voz].id)  # changing index, changes voices. 1 for female
    return engine

def vocalizacion(engine, text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("Con este programa podras hacer que tu computadora hable, segun lo que le digas.")
    text = input("Esribe lo que va a decir tu computadora: ")
    velocidad = int(input("Configura la velocidad en la que tu computadora hablara entre 100 y 150:"))
    volumen = float(input("Configura el volumen en el cual hablara tu computadora entre 0.0 y 1.0:"))
    voz = int(input("Configura en que genero hablara tu computadora 0 para Masculino 1 para Femenino:"))
    engine = configuracion(velocidad, volumen, voz)
    vocalizacion(engine, text)
    engine.save_to_file(text, "Archivo.mp3")
    engine.runAndWait()

main()