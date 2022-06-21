# fazer um código que multe o usuário caso passe de 80 km/h
velocidade = float(input('Qual a velocidade do carro no momento: '))
if velocidade > 80:  # se velocidade for maior que 80 vai executar código abaixo
    print('Voce passou de 80Km/h!!!!')
    print('Voce foi multado e o valor é R$7,00 a cada Km acima do limite!')
    multa = (velocidade * 7) - 560
    print('Sua multa é no valor de R${:.2f}'.format(multa))
else:  # caso o if acima seja falso imprimir código abaixo
    print("Bom dia, dirija com segurança, pode continuar!!")

