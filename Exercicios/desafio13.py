# peça o salário da pessoa e de um aumento de 15 no salário da pessoa
print('====== Parabens voce teve um aumento de 15% vamos recalcular seu salario =======')  # Titulo
Salario = float(input('Qual seu salario atual R$ '))  # Atribuindo valor a variavel
Aumento = (15 / 100) * Salario  # Calculando o 15%
SalarioAtual = Salario + Aumento  # Calculando o aumento
print('Voce teve um aumento de 15% que corresponde a R${:.2f}, e seu salario passa a ser R${:.2f}.'
      .format(Aumento, SalarioAtual))
# mostrando ao usuário
