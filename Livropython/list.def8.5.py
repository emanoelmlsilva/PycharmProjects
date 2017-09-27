def pesquise(lista,valor):
	for x,e in enumerate(lista):
		if e == valor:
			return x
	return None

l = [10,20,25,30]
print(pesquise(l,25))
