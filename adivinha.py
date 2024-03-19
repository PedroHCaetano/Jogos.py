import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil \
        (2) Médio \
        (3) Difícil")

    nivel = int(input("Escolha um nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range (1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou: {chute}")
        
        if(chute < 1 or chute > 100):
            print("Você precisa digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if(chute_maior):
                print(f"Você errou... O numero secreto é menor que {chute}")
            elif(chute_menor): 
                print(f"Você errou... O numero secreto é maior que {chute}")

            pontos_perdidos = abs(numero_secreto - chute) #abs() dá o valor absoluto da expressões (ignora os sinais)
            #pontos perdidos da rodada
            pontos = pontos - pontos_perdidos
            #subtraindo os pontos perdidos da pontuação total
            
    print("******Fim de jogo******")
    
if (__name__ == "__main__"):
    jogar()