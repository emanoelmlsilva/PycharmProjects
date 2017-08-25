#from random import randrange
#usando modulo
import random
x = 0
n = [0,0,0,0]
while x < 4:
	n[x] = input('aluno {} '.format(x+1))
	x+=1
lista = [n[0],n[1],n[2],n[3]]

escolha = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolha))

"""
x = 0
aluno = [0,0,0,0]
while x < 4:
	aluno [x] = str.lower(input('Informe o nome do aluno : '.format(x+1)))
	x+=1
c = randrange(4)
if(c == 0):
	alu = aluno[0]
elif(c == 1):
	alu = aluno[1]
elif(c == 2):
	alu = aluno[2]
else:
	alu = aluno[3]
print('O Aluno que iarar apagar o guadro sera:  {}'.format(alu))
"""
