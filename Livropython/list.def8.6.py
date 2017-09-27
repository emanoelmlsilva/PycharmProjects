def soma(l):
	total = 0
	for e in l:
		total+=e
	return total

def media(l):
	return(soma(l)/len(l))
l = [10,12,5]

print(media(l))
