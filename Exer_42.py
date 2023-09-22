a,b,c = map(float,input("Digite os 3 valores dos segmentos: ").split())

if a < b + c and b < a + c and c < a + b :
    print( "forma um triangulo ")
    if a == b == c:
        print("Equilátero")
    if a != b != c:
        print("Escaleno")
    else:
        print("isosceles")   
else:
    print("nao forma um triangulo")