import math 

ang = float(input("Digite seu angulo: "))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tag = math.tan(math.radians(ang))

print("Seu cosceno: é {:.2f}, seu seno: é {:.2f} e sua tangente: {:.2f}".format(cos,seno,tag))