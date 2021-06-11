import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret = random.randrange(1, 101)
    pontuacao = 1000

    print('Nível 1 - 20 chances\n'
          'Nível 2 - 10 chances\n'
          'Nível 3 - 5 chances\n')

    nivel = input("Entre com o nível: ")

    if int(nivel) == 1:
        tentativas = 20
    elif int(nivel) == 2:
        tentativas = 10
    else:
        tentativas = 5

    for tentativa in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, tentativas))

        x = input("Entre com um número entre 1 e 100: ")

        try:
            i = int(x)

            if i < 1 or i > 100:
                print("Número fora do intervalo especificado!")
                continue

            acertou = i == secret
            maior = i > secret
            menor = i < secret

            if acertou:
                print("Você acertou!")
                print("Sua pontuação é {}.".format(pontuacao))
                break
            else:
                print("Você errou!")
                if maior:
                    print("Número maior que o secreto!")
                elif menor:
                    print("Número menor que o secreto!")
                pontuacao = pontuacao - abs(secret - i)

        except ValueError:
            print("Entre com um número e não letra(s)...")

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
