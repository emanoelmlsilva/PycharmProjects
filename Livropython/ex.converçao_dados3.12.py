# Escreva um programa que calcule o tempo de uma viagem de carro
# pergunte a distancia a percorrer e a velocidade media esperada para a viagem.

distanciaPer = float(input('Informe a distancia a percorrer: '))
velocMedia = float(input('Informe a velocidade media: '))
tempoDuraçao = distanciaPer/velocMedia
print('Tempo de duração da viagem é de %4.2f h'%tempoDuraçao)
