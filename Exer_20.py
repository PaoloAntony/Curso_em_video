import random
#nao precisa de map quando é uma string vamos utilizar map para transformar oque ele digitar(srt)em inteiro(int)#
n1,n2,n3,n4 = input("Digite o nome dos alunos: ").split()
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(lista)
