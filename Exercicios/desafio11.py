# faça um calculo de quanta tinta vai precisar em uma parede, sabendo que a lata de tinta é de 2 litros
print('===== Quanto de tinta usar na parede ======')  # Titulo
largura = float(input('Coloque o largura em metros: '))  # Atribuindo uma largura em metro
altura = float(input('Coloque a altura em metros: '))  # Atribuindo uma altura em metro
area = largura * altura  # calculando a area
tinta = area / 2  # calcando a quantidade de tinta que é 2l para a area
print('Sua parede tem {}X{} e ela tem {}m² \n vai precisará de {}L de tinta'.format(largura, altura, area, tinta))
# mostrando o valor ao usuário
