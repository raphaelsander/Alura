import forca
import adivinhacao


print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")
print("(1) Forca (2) Adivinhação")

x = input("Qual jogo? ")

try:
    jogo = int(x)

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()

    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()

except ValueError:
    print("Entre com um número e não letra(s)...")
