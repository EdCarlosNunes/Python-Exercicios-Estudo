# Converter o número de metro para centimetre
print('===== Converter Metro em Centimetro! =====')  # Titulo
medida = float(input('Digite um numero em metro: '))  # Pedindo a medida em metros
cm = medida * 100  # Calculado cm
mm = medida * 1000  # Calculando em mm
print('o valor {:.1f}m é igual \n {}cm \n {}mm'.format(medida, cm, mm))  # mostrando ao usuário os valores
