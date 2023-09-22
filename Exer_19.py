import random

n1,n2,n3,n4 = (map(str,input("Digite o nome dos alunos: ").split()))

lista = [n1,n2,n3,n4]
#o random escolhe um aleatorio da lista#
rand = random.choice(lista)

print("O escolhido é: {}".format(rand))