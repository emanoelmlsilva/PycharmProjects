#Usando modulos

import random
x = 0
n = [0,0,0,0]
c=[]
while x < 4:
	n[x] = input('Aluno {} '.format(x+1))
	x+=1
#c += n
c.extend(n)
random.shuffle(c)
#lista = [n[0],n[1],n[2],n[3]]
#random.shuffle(lista)

print('A ordim de apresentação será\n {}'.format(c)) #lista))


