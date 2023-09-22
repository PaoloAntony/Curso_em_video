peso, altu = map(float,input("Digite seu peso e sua altura: ").split())

imc = peso /(altu * altu)

if imc > 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc == 25 and imc <= 30:
    print("Sobrepeso")
elif imc == 30 and imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Morbida")