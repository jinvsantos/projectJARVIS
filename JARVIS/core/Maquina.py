import pyttsx3
from settings import RATE, VOLUME, IDIOMA


class Maquina:

    def __init__(self) -> None:
        self.rate = RATE
        self.volume = VOLUME
        self.idioma = IDIOMA
        self.maquina = self.setup_maquina()

    def setup_maquina(self) -> object:
        maquina = pyttsx3.init()
        maquina.setProperty('rate', self.rate)
        maquina.setProperty('volume', self.volume)
        voices = maquina.getProperty('voices')
        voice = None
        for v in voices:
            if v.id == self.idioma:
                voice = v
        maquina.setProperty('voice', voice.id)
        return maquina
