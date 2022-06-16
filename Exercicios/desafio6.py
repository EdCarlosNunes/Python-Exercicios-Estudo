# Peça para escrever um numero e mostre o dobro, triplo e a raiz do número
print('===== Saber o dobro, triplo e raiz de um numero! =====')  # Titulo
n1 = float(input('Digite um numero: '))  # Atribuindo um float para variable n1
d = n1 + n1  # Pegando a variable n1 mais n1 e atribuído a outra variable "d"
t = n1 * 3  # Pegando a variable n1 fazendo vezes 3 e atribuído a outra variable "t"
raiz = n1 ** (1 / 2)  # fazendo o calculo da raiz da variable n1
print('o dobro de {:.0f} é {:.0f} \n o triplo de {:.0f} é {:.0f} e a raiz quadrada é {:.2f}'.format(n1, d, n1, t, raiz))
# Mostrando na tela com o format o dobro variavel "d" o triplo variavel "t" e a raiz variavel "raiz"
# {:.0f} é para tirar o numero depois da virgula pois atribui float para variavel n1
# {:.2f} para limitar apos a virgula apenas duas casa decimais
