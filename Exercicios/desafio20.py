# Essa voce vai sorta a ordem da lista de alunos que colocar também com biblioteca random
from random import *  # importando a biblioteca random com o * para não precisar usar.random
n1 = str(input("Digite um nome: "))  # como são nomes para sortear Atribui str para identificar como string
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))
nome = [n1, n2, n3, n4]   # criei uma lista para os nomes digitados acima
print('O escolhido foi essa ordem {}'.format(sample(nome, 4)))  # cham a função ‘sample’ do random para sortear um da
# lista
