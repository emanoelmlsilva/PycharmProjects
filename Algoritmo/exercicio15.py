""" Escrever um algoritmo que lê um valor em reais e calcula qual o menor número possível de
notas de 100, 50, 10, 5 e 1 em que o valor lido pode ser decomposto. Escrever o valor lido e a
relação de notas necessárias."""

valor_reais = int(input('Valor em reais: '))
c = 100
l = 50
x = 10
v = 5
i = 1
resC = valor_reais/c
valor_reais = valor_reais%c
resL = valor_reais/l
valor_reais = valor_reais%l
resX = valor_reais/x
valor_reais = valor_reais%x
resV = valor_reais/v
resI = valor_reais%v
print('A quantidade de notas de 100 é %d, 50 é %d, 10 é %d, 5 é %d, 1 é %d'%(resC,resL,resX,resV,resI))
