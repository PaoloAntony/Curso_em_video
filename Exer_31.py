distancia = float(input("Digite sua distância: "))
if distancia > 200: 
    preco = distancia * 0.45
    print("O preço é %.2f "%preco)
else:
    preco = distancia * 0.50
    print("O preço é %.2f"%preco)

