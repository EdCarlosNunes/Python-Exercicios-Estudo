# vai pedir o nome completo do usuário fala o primeiro nome e o último
nome = str(input('Digite seu nome completo: ')).strip()  # tirando espaço no começo ou final
dividir = nome.split()  # .split() O método divide uma string em uma lista
print('O seu primeiro nome é {}'.format(dividir[0]))  # chamando a primeira posição [0]
print('E seu ultimo nome é {}'.format(dividir[-1]))  # chamando a ultima [-1]
