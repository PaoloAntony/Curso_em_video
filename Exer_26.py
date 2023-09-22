nome = str(input("Digite seu nome: ")).strip()
nome = nome.upper()
a_vezes = nome.count("A")
a_comeca = nome.find("A")
a_termina = nome.rfind("A")
#rfind começa a procurar da esquerda pra direita 
print("Vezes {}, começa em {}, termina em {} ".format(a_vezes,a_comeca +1,a_termina +1))