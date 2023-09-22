num = int(input("Digite seu numero: "))
primnum = 1
for n in range(10):
    result = num * primnum
    print("{} x {} = {}".format(primnum,num,result)) 
    primnum += 1
