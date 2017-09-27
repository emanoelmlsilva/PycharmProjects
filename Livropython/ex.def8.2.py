
int1 = int(input('valor 1: '))
int2 = int(input('valor 2: '))
def multiplo(int1,int2):
	if int1 % int2 == 0:
		return True
	else:
		return False

print(multiplo(int1,int2))
