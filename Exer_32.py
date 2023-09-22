from datetime import date 
#biblioteca para pegar ano da propia maquina no caso 2023 que nao é bissexto
#funcaozinha pra pegar  o ano da maquina quando digitar 0 

ano = int(input("Digite o ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4==0 and ano %100 != 0 or ano % 400 == 0:
    print("É ano bissexto")
else:
    print("Não é ano bissexto")