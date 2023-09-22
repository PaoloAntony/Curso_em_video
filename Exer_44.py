print("Opções:\n 1 = Dinheiro/Cheque\n 2 = 1x Cartão\n 3 = 2x no cartão\n 4 = 3x ou mais ")
prec, cond = map(int,input("Digite o preço e a condição de pagamento: ").split())
if cond == 1:
   result = prec - (prec * 10 /100)
   print(result)

elif cond == 2:
    result = prec - (prec * 5/100)
    print(result)

elif cond == 3:
    result = prec /2
    print(result)

elif cond == 4:
    result = prec - (prec * 20 / 100)
    print(result)

    
