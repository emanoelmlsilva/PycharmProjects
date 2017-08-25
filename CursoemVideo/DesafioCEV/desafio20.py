#from random import randrange
#Usando modulos
import random
x = 0
n = [0,0,0,0]
while x < 4:
	n[x] = input('Aluno {} '.format(x+1))
	x+=1

lista = (n[0],n[1],n[2],n[3])

random.shuffle([lista])

print('A ordim de apresentação será\n {}'.format(lista))

"""
x = 0
aluno = [0,0,0,0]
aux = [0,0,0,0]

while x < 4:
	aluno[x] = str(input('Informe o nome do  aluno '))
	x+=1

x = 0
z = 0
dif = [0,0,0,0]
while x < 4:
	aux[x] = randrange(4)
	print('num1',aux[x])
	cont = 0
	v = 0
	while cont <= x:
		if(aux[x] == dif[cont]):
			v += 1
		elif(cont == x and v > 0):
			aux[x] = randrange(4)
			print('num2',aux[x])
			cont = 0
		cont+=1
	dif[z] = aux[x]
	print('O aluno {} sera o {} á apresentar '.format(aluno[x],aux[x]+1))
	x+=1
	z+=1
"""


