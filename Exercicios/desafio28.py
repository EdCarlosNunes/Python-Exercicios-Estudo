#  criar um jogo com o usuário pedir para ele tentar acertar qual numero a máquina escolhe de 0 a 5
from random import randint  # importando biblioteca random
from time import sleep  # importando a biblioteca time
print('Vamos brincar!')
print('Vou pensar em um numero de 0 a 5 e voce tem que acerta')
print('-=-'*20)
numero = int(input("Digite o numero que acha que é: "))  # pedir o número para o usuário
sorte = randint(0, 5)  # aqui vai ser a opção para a máquina
print('Processadno....')  # aparecer um processando
sleep(1)  # para esperar e não aparecer de uma vez da biblioteca time
if numero == sorte:  # se numero do usuário for igual == a sorteio máquina
    print('Parabens Voce acerto!!')  # imprimir voce acerto
else:  # caso seja falso imprimir o else
    print('Voce errou, eu pensei no numero {} e não no {}, tente novamente!'.format(sorte, numero))
