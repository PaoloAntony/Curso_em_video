from random import randint

computador = randint(0,5)
numero = int(input("Digite o numero: "))
if numero == computador:
    print("Você Acertou")
else:
    print("Você Errou ")

