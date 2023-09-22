prod = float(input("Preço: R$: "))
descont = prod - (prod * 5) /100
print("Seu desconto é de: R$: {:.2f}".format(descont))