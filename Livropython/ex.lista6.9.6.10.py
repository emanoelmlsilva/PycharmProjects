l = [15,7,27,39]

p = int(input('Digite o valor a procurar: '))
v = int(input('Digite o valor a procurar: '))
x = 0
contp = 0
contv = 0
primeiro = 0
for x in range(len(l)):
#while x < len(l):
	if l[x] == p:
		contp = 1
		po = x
		if primeiro == 0:
			primeiro = l[x]
	if l[x] == v :
		contv = 2
		vo = x
		if primeiro == 0:
			primeiro = l[x]
	if contp == 1 and contv == 2:
		break
#	x+=1
if contp == 1:
	print('{} achado na posição {}'.format(p,po))
else:
	print('{} não encontrado'.format(p))
if contv == 2:
	print('{} achado na posição {}'.format(v,vo))
else:
	print('{} não encontrado'.format(v))
print('encontrado primeiro foi {}'.format(primeiro))

"""if po <= vo:
	print('encontrado primeiro foi {}'.format(po))
else:
	print('encontrado primeiro foi {}'.format(vo))"""

