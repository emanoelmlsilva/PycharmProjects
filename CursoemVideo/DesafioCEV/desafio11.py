"""Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua area e a
quantidade de tinta necessária para pintá-lo.Sabendo que cada litro de tinta, pinta uma area de 2m²."""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
quant = area / 2
print('A area de parede é {}m² e a quantidade de tinta necessaria para pintar é {}L'.format(area,quant))