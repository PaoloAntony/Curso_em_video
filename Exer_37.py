

print("1 == Converter para BINARIO\n2 == Converter para OCTONAL\n3 == Converter para HEXADECIMAL")
num,cov = map(int,input("Digite o número e qual conversão você deseja:").split())
#funçoes bin,oct e hex para binario,octonal e hex 

if cov == 1:
    print (bin(num))
elif cov == 2:
    print(oct(num))
elif cov == 3:
    print(hex(num))





