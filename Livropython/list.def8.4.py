def épar(x):
	return(x%2==0)

def par_ou_impar(x):
	if épar(x):
		return 'Par'
	else:
		return 'Impar'
print(par_ou_impar(4))
print(par_ou_impar(5))
