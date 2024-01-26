import pywhatkit
import wikipedia
import datetime
from settings import LANG_WIKIPEDIA


class Comandos:

    def __init__(self, maquina) -> None:
        self.maquina = maquina

    def jarvis(self) -> None:
        self.maquina.say('Em que posso ajudar o senhor?')
        self.maquina.runAndWait()

    def horas(self) -> None:
        hora = datetime.datetime.now().strftime('%H:%M')
        self.maquina.say(f'Agora são {hora}')
        self.maquina.runAndWait()

    def wikipedia(self) -> None:
        procurar = input("O que deseja procurar? ")
        wikipedia.set_lang(LANG_WIKIPEDIA)
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        self.maquina.say(resultado)
        self.maquina.runAndWait()

    def tocar_musica(self) -> None:
        musica = input('Nome da musica: ')
        self.maquina.say(f'Tocando Musica {musica}')
        self.maquina.runAndWait()
        pywhatkit.playonyt(musica)

    def erro(self) -> None:
        self.maquina.say('Me perdoe senhor, nao entendi o comando')
        self.maquina.runAndWait()
