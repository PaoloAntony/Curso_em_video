nota1, nota2 = map(float,input("Diite sua primeira nota e sua segunda nota: ").split())

media = (nota1 + nota2) /2

if media < 5.0:
    print("Reprovado")
elif media >= 7.0:
    print("Aprovado")
elif media >= 5.00 or media >= 6.9:
    print("Recuperação")