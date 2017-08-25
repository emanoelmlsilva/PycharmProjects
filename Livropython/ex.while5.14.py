""" Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até
que o usuário digite 0(zero). No final da execução, exiba a quantidade de números digitados, assim
como a soma e a média aritmética."""
cont = 0
soma = 0
while True:
    num_int = int(input('Informe o numero: '))
    if(num_int != 0):
        soma += num_int
        cont += 1
    else:
        break
med_arit = soma / cont
print('soma: %d'%soma)
print('Quantidade: %d'%cont)
print('Media aritmética: %3.2f'%med_arit)