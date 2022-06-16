# Digitar um numero entre 0 e 9999 e falar qual é a unidade, dezena centena e milhar
num = int(input('Digite um numero de 0 a 9999: '))  # pedindo para digitar um valor
u = num//1 % 10  # calculo de unidade
d = num//10 % 10  # calculo de dezena
c = num//100 % 10  # calculo da centena
m = num//1000 % 10  # calculo da milhar

print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
# mostrar os numero na tela
