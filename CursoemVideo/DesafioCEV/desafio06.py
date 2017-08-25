# Crie um algoritmo que leia um número e mostre o seu dobro , triplo e raiz quadrada.

num = int(input('Digite um número: '))
d = num*2
t = num*3
r = num**(1/2)
print('dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(num,d,t,r))