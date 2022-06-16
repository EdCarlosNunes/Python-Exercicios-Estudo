# calcule o seno, cosseno e tangente com a biblioteca math
from math import *  # importando a biblioteca math e com o * tiro a necessidade de colocar.math
angulo = float(input('Digite um angulo: '))  # peço o valor para atribuir
sen = sin(radians(angulo))  # calculando o seno com a biblioteca math
cos = cos(radians(angulo))  # calculando o cosseno com a biblioteca math
tag = tan(radians(angulo))  # calculando o tangente  com a biblioteca math
print('Com um angulo {:.0f}º\n O seno é {:.3f}\n O cosseno {:.3f}\n A tangente {:.3f}'.format(angulo, sen, cos, tag))
# mostra o valor com a resposta usando o format
