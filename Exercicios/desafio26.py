# peça o nome do usuario informe quantas letras a tem o nome e qual a primeira posição e a última que encontra a letra a
nome = str(input('Digite o seu nome inteiro: ')).strip().lower()
print('O seu nome tem {} letras a'.format(nome.count('a')))
print('O primeiro a no seu nome esta na posição {}º'.format(nome.find('a')+1))
print('A ultima posição da letra a no seu nome é {}º'.format(nome.rfind('a')+1))
