from core.Comandos import Comandos
from core.Maquina import Maquina
from core.Speech import Speech
from core.auxiliares import clean

if __name__ == "__main__":
    maq = Maquina()
    sp = Speech()
    comando = Comandos(maquina=maq.maquina)

    while True:
        clean()
        print("'desativar' para fechar o assistente".upper())
        fala = sp.ouvindo()
        if fala == "jarvis":
            comando.jarvis()
        elif (fala == "horas"):
            comando.horas()
        elif (fala == "wikipedia"):
            comando.wikipedia()
        elif (fala == "tocar musica"):
            comando.tocar_musica()
        elif (fala == "desativar"):
            break
        else:
            comando.erro()
