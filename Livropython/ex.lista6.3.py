l1=[0]
l2=[0]
l3=[]
l4=[]
x=0
num = 1
while num != 0:
	num = int(input('Digite o {}ª valor: '.format(x+1)))
	x+=1
	l1.append(num)

y=0
num2 = 1
while num2 != 0 :
	num2 = int(input('Digite o {}ª valor: '.format(y+1)))
	y+=1
	l2.extend([num2])

""" OU
z=0
while z < len(l1):
	cont=0
	v=0
	while cont < len(l2):
		if(l1[z] == l2[cont]):
			v+=1
		cont+=1
	if v == 0:
		l4.append(l1[z])
	z+=1

z=0
while z < len(l2):
        cont=0
        v=0
        while cont < len(l1):
                if(l2[z] == l1[cont]):
                        v+=1
                cont+=1
        if v == 0:
                l4.append(l2[z])
        z+=1

"""
z=0
while z < len(l1):
        cont=0
        v=0
        while cont < len(l2):
                if(l1[z] != l2[cont]):
                        v+=1
                cont+=1
        if v == len(l2):
                l4.append(l1[z])
        z+=1

z=0
while z < len(l2):
        cont=0
        v=0
        while cont < len(l1):
                if(l2[z] != l1[cont]):
                        v+=1
                cont+=1
        if v == len(l1):
                l4.append(l2[z])
        z+=1


print(l4)

i=0
while i < len(l4):
	print('{}, {}'.format(i,l4[i]))
	i+=1

