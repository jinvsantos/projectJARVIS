import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.setProperty('rate', 100)

def comando_de_voz():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='en-us')
            comando = comando.lower()
    except:
        print('Wait a sec...')
    return comando

def comandos(fala):
    if('time' == fala):
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif ('find' == fala):
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif ('play' == fala):
        maquina.say("Please say music name")
        maquina.runAndWait()

        musica = comando_de_voz()
        maquina.say(f'Tocando Musica {musica}')
        maquina.runAndWait()
        resultado = pywhatkit.playonyt(musica)

fala = comando_de_voz()
print(f'Your command is: {fala}')
comandos(fala)