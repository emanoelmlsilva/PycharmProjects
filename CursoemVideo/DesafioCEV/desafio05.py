#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero: '))
x = 1
y = 1
x = num - x
y += num
print('antecessor {} , de {} e o sucessor {}'.format(x,num,y))