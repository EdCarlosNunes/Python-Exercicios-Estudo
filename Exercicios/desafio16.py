# o usuário vai digitar o valor quebrado e voce mostra a porção inteira do número
from math import trunc  # importando a biblioteca math
print('Digite um numero com virgula e aparece a porção inteira')  # Titulo
Num = float(input('Digite um numero: '))  # atribuindo um número
print('o valor digitado foi {}e a porção itera é {}'.format(Num, trunc(Num)))
# mostrando ao usuário o valor
