from comandos import comandoDeVoz, horas, pesquisaWikipedia, tocarYoutube
from playsound import playsound


playsound("JARVIS/audio/suaDisposicao.mp3")

comando = comandoDeVoz()
if('horas' == comando):
    horas()
elif ('pesquisar' == comando):
    pesquisaWikipedia()
elif ('tocar' == comando):
    tocarYoutube()