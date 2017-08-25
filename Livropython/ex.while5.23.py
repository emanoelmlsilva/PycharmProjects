"""Escreva um programa que leia um número e verifique se é ou não um número primo.Para
fazer essa verificalçao, calcule o resto da divisao do número por 2 e depois por todos
os números impares até o numero lido.Se o resto de uma dessas divisoes for igual a zero,
o número não é primo.Observe que 0 e 1 não são primos e que 2 é o único número primo que é par"""

num = int(input('Infome o numero que deseja saber se é primo ou não: '))
cont = 1
s = 0
while cont <= num:
    if(num % cont == 0):
        s += 1
    cont+=1
if(s == 2):
    print('{} é primo'.format(num))
else:
    print('{} não é primo'.format(num))