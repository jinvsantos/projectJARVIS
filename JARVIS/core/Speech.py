import speech_recognition as sr
from settings import LANG_SPEECH, DEBUG_SPEECH


class Speech:

    def __init__(self):
        self.idioma = LANG_SPEECH
        self.audio = sr.Recognizer()

    def ouvindo(self):
        try:
            with sr.Microphone() as source:
                if DEBUG_SPEECH:
                    comando = input("comando: ")
                else:
                    voz = self.audio.listen(source)
                    comando = self.audio.recognize_google(
                        voz, language=self.idioma)
                comando = comando.lower()
                return comando
        except:
            print('Wait a sec...')
