# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuario,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km_percorrido = float(input('Informe a quantidade de Km precorrido: '))
dias_alugado = int(input('Informe a quantidade de dias que o carro passou alugado: '))
preço_pagar = km_percorrido*0.15 + dias_alugado*60
print('A preço do alugel do carro é de %5.2f R$'%preço_pagar)