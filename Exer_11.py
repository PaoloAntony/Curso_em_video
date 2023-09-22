larg,alt = map(int,input("Digite a largura e a altura da parede: ").split())
area = larg * alt
tinta = area / 2
print ("A dimensão seria {}x{},\n portanto sua Área é {} \n e seriam necessários {} baldes de tinta ".format(larg,alt,area,tinta))