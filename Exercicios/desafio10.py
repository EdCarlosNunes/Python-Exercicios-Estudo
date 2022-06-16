# Pegue um valor em real e converta em dollar e euro
print('===== Converter real para dolar e euro! ======')  # titulo
n1 = float(input('Quanto tem em R$'))  # pendendo o valor para converter
dolar = n1 / 5.06  # calculo para converter em dollar, valor atual de 2022
euro = n1 / 5.28  # calculo para converter em euro, valor atual de 2022
print('Voce tem R${:.2f} em dolar US${:.2f} e euro EUR${:.2f}'.format(n1, dolar, euro))
# mostrando ao usuário os valores com format
