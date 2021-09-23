import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()

maquina = pyttsx3.init()
maquina.setProperty('rate', 120)

wikipedia.set_lang('pt')

def comando_de_voz():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-br')
            comando = comando.lower()
    except:
        print('Wait a sec...')
    return comando

def comandos(fala):
    if('horas' == fala):
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif ('pesquisar' == fala):
        maquina.say(f"O que pesquisar?")
        maquina.runAndWait()

        pesquisa = comando_de_voz()
        maquina.say(f"Pesquisando {pesquisa} no wikipedia")
        maquina.runAndWait()

        resultado = wikipedia.summary(pesquisa, sentences=1)
        maquina.say(resultado)
        maquina.runAndWait()

    elif ('tocar' == fala):
        maquina.say("Por favor diga o nome da musica:")
        maquina.runAndWait()

        musica = comando_de_voz()
        maquina.say(f'Tocando Musica {musica}')
        maquina.runAndWait()
        resultado = pywhatkit.playonyt(musica)

fala = comando_de_voz()
comandos(fala)