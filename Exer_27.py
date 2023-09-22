nome = str(input("Digite seu nome completo: ")).strip()
nome = nome.split()
#com o split separamos o nome em partes no caso nome nome do meio e sobrenome
#com len lemos o numero de separaçoes que temos no nome e pegamos a ultima
#o colchete serve pra procurar na posiçao como se fosse [0:3]
ultimonome = nome[len(nome)-1]
print("primeiro nome {}, Ultimo nome {}".format(nome[0],ultimonome))