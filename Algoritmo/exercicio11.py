""" O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de
fábrica de um carro e escreva o custo ao consumidor."""

custo_fabrica = float(input('Custo de fabrica: '))
percent_distribu = 0.28
impostos = 0.45
custo_consumidor = (percent_distribu+impostos * custo_fabrica) + custo_fabrica
print('Custo ao consumidor é de %5.2f R$'%custo_consumidor)