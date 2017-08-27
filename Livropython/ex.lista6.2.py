l1=[0]
l2=[0]
l3=[]
x = 0
y = 0
z = 0
while x < len(l1):
	num = int(input('Informe o valor {}: '.format(x+1)))
	x+=1
	if num == 0:
		break
	l1+=[num] #ou l1.append(num)
while y < len(l2):
	num2 = int(input('Digite o valor {}: '.format(y+1)))
	y+=1
	if num2 == 0:
		break
	l2.extend([num2]) #ou l2.append(num2)

#l3.append([l1,l2])
#l3.extend([l1,l2])
l3+=[l1+l2]
while z < len(l3):
	print(l3[z])
	z+=1

