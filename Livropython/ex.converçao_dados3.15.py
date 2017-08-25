# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# pergunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarros,
# calcule quantos dias de vida um fumante perdera. exiba o valor em dias.

cigarro_dia = int(input('Informe a quantidade de cigarros fumados por dias: '))
anos = float(input('Informe a quantidade de anos que ja fumou: '))
minutos = 10*cigarro_dia
res = (minutos/1440) + (anos * 365)
print('O valor de dias perdidos é de %5.2f'%res)

