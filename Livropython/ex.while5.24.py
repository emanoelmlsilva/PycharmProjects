"""Modifique o programa anterior de forma a ler um número n.Imprima os n primeiros números primos"""

num = int(input('Infome o numero que deseja saber se é primo ou não: '))
n = 2
while n <= num:
    cont = 1
    s = 0
    while cont <= n:
        if(n % cont == 0):
            s += 1
        cont+=1
    if(s == 2):
        print('{} é primo'.format(n))
    n += 1