import pyttsx3
from settings import RATE, VOLUME, IDIOMA


class Maquina:

    def __init__(self) -> None:
        self.rate = RATE
        self.volume = VOLUME
        self.idioma = IDIOMA
        self.maquina = self.setup_maquina()

    def setup_maquina(self):
        maquina = pyttsx3.init()

        """Velocidade"""
        maquina.setProperty('rate', self.rate)

        """ VOLUME """
        maquina.setProperty('volume', self.volume)

        """ VOICE """
        voices = maquina.getProperty('voices')
        voice = None
        for v in voices:
            if v.id == self.idioma:
                voice = v
        maquina.setProperty('voice', voice.id)

        return maquina
