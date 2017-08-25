"""Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao
usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de côdigos abaixo
para obter o preço de cada produto:"""

tot = 0
while True:
    print('\nCódigo  =   Preço')
    print('  1          0.50')
    print('  2          1.00')
    print('  3          4.00')
    print('  5          7.00')
    print('  9          8.00')
    print('  0         Parar\n')
    codigo = int(input('Informe  o codigo do produto: '))
    if codigo == 0:
        break
    elif (codigo != 1) and (codigo != 2) and (codigo != 3) and (codigo != 5) and (codigo != 9):
        print('Código inválido')
        break
    quanti_compra = float(input('informe a quantidade de comprada: '))
    if codigo == 1:
        quanti_compra *= 0.50
    elif codigo == 2:
        quanti_compra *= 1.00
    elif codigo == 3:
        quanti_compra *= 4.00
    elif codigo == 5:
        quanti_compra *= 7.00
    elif codigo == 9:
        quanti_compra *= 8.00
    #else:
     #   print('Código inválido')
    tot += quanti_compra
print('Total das Compras %4.2f'%tot)
