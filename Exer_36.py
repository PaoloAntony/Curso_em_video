valcas, sal,anopag = map(int,input("Valor da casa,seu sálario e em quanto tempo \nvai pagar: ").split())

parcela = valcas / (anopag * 12)
min = sal * 30 /100

if parcela <=  min:
    print("EMPRESTIMO APROVADO")
else:
    print("EMPRESTIMO NEGADO")
