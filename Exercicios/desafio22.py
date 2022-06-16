# peca para o usuário escrever o nome completo, retornar o nome em maiúscula e minuscula
# quantas letras tem sem contar com os espaços e qual o primeiro nome e quotas letras o primeiro nome tem
nome = str(input("Digite seu nome completo: ")).strip()  # atribuindo str para string e . strip() para eliminar
# espaço no começo e no final caso o usuário de espaço no começo ou no final
dividir = nome.split()
sem = nome.replace(' ', '')  # .replace ele substitute algo por algo no caso onde tem espaço fica sem
print('Seu nome em maiúscula: {}'.format(nome.upper()))  # .upper para deixar tudo maiúscula
print('Seu nome em minúscula: {}'.format(nome.lower()))  # .lower para deixar tudo minuscula
print('Seu nome tem: {} letras'.format(len(sem)))  # len conta os caracteres
print('Seu primeiro é {} e tem: {} letras'.format(dividir[0], len(dividir[0])))
# primeiro pego a variable e puxo a posição [0] e o segundo puxo a posição [o] com o len para contar
