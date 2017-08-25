# Escreva um programa que leia tres numeros e que imprima o maior e o menor
num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))
if((num1 > num2) and (num1 > num3)):
    print('%d é o Maior numero'%num1)
if((num2 > num1) and (num2 > num3)):
    print('%d é o Maior numero'%num2)
if((num3 > num2) and (num3 > num1)):
    print('%d é o Maior numero'%num3)
if ((num1 < num2) and (num1 < num3)):
    print('%d é o menor numero' % num1)
if ((num2 < num1) and (num2 < num3)):
    print('%d é o menor numero' % num2)
if ((num3 < num2) and (num3 < num1)):
    print('%d é o menor numero' % num3)