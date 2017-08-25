"""Escreva um programa que exiba uma lista de opçoes(menu):adiçao,subtraçao,divisao,
multiplicaçao e sair.Imprima a tabuada da opraçao escolhida.Repita ate que a opçao
escolhida."""

while True:
    print('1 para Adição')
    print('2 para Subtração')
    print('3 para Divisão')
    print('4 para Multiplicação')
    print('0 para Sair')
    escolha = int(input('>>>'))
    cont = 1
    if(escolha == 0):
        print('Programa parado')
        break
    else:
        num = int(input('Digite o número da tabuada: '))
        if(escolha == 1):
            while cont <= 10:
                print('{} + {} = {}'.format(num,cont,num+cont))
                cont += 1
        elif(escolha == 2):
            while cont <= 10:
                print('{} - {} = {}'.format(num,cont,num-cont))
                cont += 1
        elif(escolha == 3):
            while cont <= 10:
                print('{} / {} = {:.2f}'.format(num,cont,num/cont))
                cont += 1
        elif(escolha == 4):
            while cont <= 10:
                print('{} * {} = {}'.format(num,cont,num*cont))
                cont += 1

