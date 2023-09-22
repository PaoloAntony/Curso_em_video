km = float(input("Digite os km: "))
dias = int(input("Digite os dias: "))

paga = (km * 0.15) + (dias * 60)
print ("O total a pagar é de R$: {:.2f}".format(paga))