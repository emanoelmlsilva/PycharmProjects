# Escreva um programa que leia uma valor em metros e o exiba convertido em milimetros

metro = float(input('Informe o valor em metros: '))
mil = metro*1000
print('A conversão de %3.2f metro para milimetros é %5.2f '% (metro,mil))