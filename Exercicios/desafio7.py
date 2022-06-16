# Peça para colocar duas notas e calcule a média
print('===== Calcular media de 2 notas! =====')  # Titulo
n1 = float(input('Digite sua primeira nota: '))  # pedir para atribuir uma nota na variavel n1
n2 = float(input('Digite sua segunda nota: '))  # pedir para atribuir uma nota para variavel n2
media = (n1 + n2) / 2  # calculando  a media das duas variaveis n1 e n2
print('Sua media é: {:.1f}'.format(media))  # mostrar ao usuário a média com format
