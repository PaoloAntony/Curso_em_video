import math

co,ca = map(float,input("Digite o cateto oposto e em seguida o adjacente: ").split())
hi = math.hypot(co,ca)

print("A hipotenusa mede {:.2f}".format(hi))