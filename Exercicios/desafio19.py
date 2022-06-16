# digite 4 nomes e faça um sorteio dos nome e mostre apenas um com a biblioteca random
from random import *  # importando a biblioteca random com o * para não precisar usar.random
n1 = str(input("Digite um nome: "))  # como são nomes para sortear Atribui str para identificar como string
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))
nome = [n1, n2, n3, n4]  # criei uma lista para os nomes digitados acima
print('O escolhido foi {}'.format(choice(nome)))  # cham a função choice do random para sortear um da lista
