import pywhatkit
import wikipedia
import datetime
from settings import LANG_WIKIPEDIA


class Comandos:

    def __init__(self, maquina):
        self.maquina = maquina

    def jarvis(self):
        self.maquina.say('Em que posso ajudar o senhor?')
        self.maquina.runAndWait()

    def horas(self):
        hora = datetime.datetime.now().strftime('%H:%M')
        self.maquina.say(f'Agora são {hora}')
        self.maquina.runAndWait()

    def wikipedia(self):
        procurar = input("O que deseja procurar? ")
        wikipedia.set_lang(LANG_WIKIPEDIA)
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        self.maquina.say(resultado)
        self.maquina.runAndWait()

    def tocar_musica(self):
        musica = input('Nome da musica: ')
        self.maquina.say(f'Tocando Musica {musica}')
        self.maquina.runAndWait()
        pywhatkit.playonyt(musica)

    def erro(self):
        self.maquina.say('Me perdoe senhor, nao entendi o comando')
        self.maquina.runAndWait()
