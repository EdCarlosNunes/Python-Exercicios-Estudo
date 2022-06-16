# pegue o cateto oposto e o adjacente e calcule a hipotenusa
import math  # importando a biblioteca math
co = float(input('coloque o valor do cateto oposto: '))  # atribuindo um valor ao cateto oposto
adj = float(input('Coloque o valor do cateto adjacente: '))  # Atribuindo um valor ao cateto adjacente
hipotenusa = math.hypot(co, adj)  # calculando a hipotenusa com a biblioteca math
# hipotenusa = (co ** 2 + adj ** 2) ** (1/2) calculando sem a biblioteca math
print('Hipotenusa é igual a {:.2f}'.format(hipotenusa))  # mostrando ao usuário o resultado
