a,b,c = map(float,input("Digite os 3 valores dos segmentos: ").split())

if a < b + c and b < a + c and c < a + b :
    print( "forma um triangulo ")
else:
    print("nao forma um triangulo")