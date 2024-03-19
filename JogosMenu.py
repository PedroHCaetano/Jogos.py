import adivinha
import Forca

def escolhe_jogo():

    print("*********************************")
    print("Bem vindo ao Menu de jogos!")
    print("*********************************")

    print("Escolha o seu jogo:")

    print("(1) Adivinha \
        (2) Forca")

    jogo = int(input("Digite o número do jogo escolhido: "))

    if (jogo == 1): 
        print("Carregando jogo da Adivinha...")
        adivinha.jogar()
    elif (jogo == 2):
        print("Carregando o jogo da Forca...")
        Forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()