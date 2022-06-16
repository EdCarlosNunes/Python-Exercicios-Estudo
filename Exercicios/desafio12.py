# coloque um valor e ele te da o valor com um desconto de 5%
print('===== Desconto de 5% de desconto na loja toda')  # Titulo
ValorProduto = float(input('Qual o valor do produto R$: '))  # Atribuindo um valor para produto
Desconto = (5 / 100) * ValorProduto  # calculando 5% do valor atribuindo a vriavel
ValorComDesconto = ValorProduto - Desconto  # calculando o valor do desconto
print('O produto no valor de R${:.2f}, teve um desconto de R${:.2f} e o valor passa a ser R${:.2f}'
      .format(ValorProduto, Desconto, ValorComDesconto))
# Mostrar ao usuário o valor com desconto
