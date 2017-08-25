""" Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento.
Para salarios superiores a R$ 1.250,00, calcule um aumento de 10%.Para os inferiores de 15%"""

salario = float(input('Qual o salario: '))
if(salario > 1250):
    aumento = 0.10
    calc_aumento = (salario * aumento) + salario
    print('salario atual é de %5.2f'%calc_aumento)
if(salario < 1250):
    aumento = 0.15
    calc_aumento = (salario * aumento) + salario
    print('Salario atual é de %5.2f'%calc_aumento)