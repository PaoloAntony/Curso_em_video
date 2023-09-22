salario = float(input("Digite seu salário: "))
if salario > 1250.00:
    novosal = (salario * 10 /100) + salario 
else:
    novosal = (salario * 15 /100) + salario 

print("Salario antigo {:.2f}, salario novo {:.2f}".format(salario,novosal))
