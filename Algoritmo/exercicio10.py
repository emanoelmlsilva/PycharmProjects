"""Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em
segundos e mostre-o expresso em horas, minutos e segundos."""

temp_second = int(input('Informe o tempo de duração de um evento de uma fábrica em segundos: '))
horas = temp_second/3600
minutos = (temp_second%3600)/60
segundos = (temp_second%3600)%60
print('A duraçao é %d horas, %d minutos, %d segundos'%(horas,minutos,segundos))