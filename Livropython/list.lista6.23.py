l = [15,7,27,39]
p = int(input('Digite o valor a procurar: '))
achou = False
x = 0
while x < len(l):
	if l[x] == p:
		achou = True
		break
	x+=1

if achou == True:
	print('{} achdo na posição {}'.format(p,x))
else:
	print('{} não encontrado'.format(p))
