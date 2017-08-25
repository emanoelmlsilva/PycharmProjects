"""Escreva um programa que calcule o resto da divisão inteira entre dois números.Utilize apenas
as operaçoes de somar e subtração para calcular o resultado."""

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
q = 0
"""
simples
r = num1
while r > num2:
    r -= num2
    q += 1
print('resto {}'.format(r))"""
if num1 > num2:
    r = num1
    while r >= num2:
        r -= num2
        q+=1
    print('resto da divisão é {}'.format(r))
else:
    r = num2
    while r >= num1:
        r -= num1
        q += 1
    print('resto da divisão é {}'.format(r))
