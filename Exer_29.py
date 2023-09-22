vel = int(input("Digite a velocidade: "))
if vel > 80:
   multa =  ( vel - 80 ) *7
   print("Sua multa é de R$ {},00".format(multa))
else:
     print("Não houve multa")