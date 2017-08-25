# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares
# ela pode comprar. (Considere US$1.00 = R$3.27)

dinheiro = float(input('Informe aquantidade dinheiro na carteira: '))
dolar = dinheiro/3.27
print('Quatidade de dorales que pode comprar é {:.2f}US$'.format(dolar))
