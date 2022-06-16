# pegar o nome e ver se é silva se for mostrar true
nome = str(input('Digite o seu nome completo: ')).strip()  # atribuindo str para string e . strip() para eliminar
p = nome.lower()  # para não ter erro coloque tudo em minusculo com o .lower
Silva = 'silva' in p  # vejo se "silva" é igual a variable cidade
print('O nome seu nome {} Silva'.format(Silva))  # da o retorno se é true or false
