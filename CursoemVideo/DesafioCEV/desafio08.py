# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros.

metros = float(input('Digite a quantidade em metros: '))
c = metros * 100
m = metros * 1000
print('Conversao de {} metros em centimetros é {:.2f} e em milimetros é {}'.format(metros,c,m))