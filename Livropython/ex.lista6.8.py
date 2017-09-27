l = [15,7,27,39]

p = int(input('Digite o valor a procurar: '))

x = 0
cont = 0
while x < len(l):
	if l[x] == p:
		cont = 1
		break
	x+=1
if cont == 1:
	print('{} achado na posição {}'.format(p,x))
else:
	print('{} não encontrado'.format(p))
