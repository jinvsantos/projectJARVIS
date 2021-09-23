import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr
import pyttsx3

#RECONHECIOMENTO DE FALA
audio = sr.Recognizer()

#FALA DO COMPUTADOR
maquina = pyttsx3.init()
maquina.setProperty('rate', 120)

#CONFIGURACOES DO WIKIPEDIA PARA PESQUISA
wikipedia.set_lang('pt')


def comandoDeVoz():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-br')
            comando = comando.lower()
    except:
        print('Wait a sec...')
    return comando

def horas():
    hora = datetime.datetime.now().strftime('%H:%M')
    maquina.say('Agora são' + hora)
    maquina.runAndWait()

def pesquisaWikipedia():
    maquina.say(f"O que pesquisar?")
    maquina.runAndWait()
    pesquisa = comandoDeVoz()
    maquina.say(f"Pesquisando {pesquisa} no wikipedia")
    maquina.runAndWait()
    resultado = wikipedia.summary(pesquisa, sentences=1)
    maquina.say(resultado)
    maquina.runAndWait()

def tocarYoutube():
    maquina.say("Por favor diga o nome da musica:")
    maquina.runAndWait()
    musica = comandoDeVoz()
    maquina.say(f'Tocando Musica {musica}')
    maquina.runAndWait()
    resultado = pywhatkit.playonyt(musica)