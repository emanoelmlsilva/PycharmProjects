#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do prduto: '))
newpreço = preço - preço * 0.05
print('O novo valor do produto é {}R$'.format(newpreço))
