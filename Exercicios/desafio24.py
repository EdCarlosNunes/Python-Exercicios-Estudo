# pegar o nome da cidade e ver se é santos se for mostrar true
cidade = str(input('Digite o nome da sua cidade: ')).strip()  # atribuindo str para string e . strip() para eliminar
p = cidade.lower()  # para não ter erro coloque tudo em minusculo com o .lower
santos = 'santo' in p  # vejo se "santos" é igual a variable cidade
print('O nome da sua cidade {} Santos'.format(santos))  # da o retorno se é true or false
