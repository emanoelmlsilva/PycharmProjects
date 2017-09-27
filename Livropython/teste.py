lista = []
while True:
	valor= int(input('Informe um valor: '))
	if valor == 0:
		break
	livro=input('Informe o nome do livro: ')
	lista.append([livro,valor])
print(lista)
