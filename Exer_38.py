val1,val2 = map(int,input("Digiste os dois valores: ").split())

if val1 > val2:
    print("%d É maior"%val1)
elif val2 > val1:
    print("%d É maior"%val2)
elif val1 == val2:
    print("Valores iguais")
elif val2 == val1:
    print("Valores iguais ")

