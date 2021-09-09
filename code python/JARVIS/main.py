import speech_recognition as sr
import pyttsx3
import pyaudio

audio = sr.Recognizer()
maquina = pyttsx3.init()


try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'jarvis' in comando:
            print(comando)
            maquina.say(comando)
            maquina.runAndWait()
except:
    print('Microfone não esta ok')

