from datetime import date 

anolist = int(input("Ano que nasceu: "))

anohoje = date.today().year

idade = anohoje - anolist

if idade < 18:
    print("não é hora de se alistar")

elif idade >18:
    print("Ja passou o tempo para o alistamento")

elif idade == 18:
    print("Hora de se alistar!")