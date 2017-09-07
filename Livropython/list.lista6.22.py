prato = 0
pilha = list(range(prato))
while True:
	print('\nExistem {} pratos na pilha'.format(len(pilha)))
	print('Pilha atual: {}'.format(pilha))
	print('Digite E para empilhar um novo prato',end=' ')
	print('ou D para desempilhar. S para sair.')
	operaçao = input('Operação (E, D ou S): ')
	if operaçao == 'D':
		if(len(pilha))>0:
			lavado = pilha.pop(-1)
			print('Prato {} lavado'.format(lavado))
		else:
			print('Pilha vazia! Nada para lavar.')
	elif operaçao == 'E':
		prato += 1 # novo prato
		pilha.append(prato)
	elif operaçao == 'S':
		break

	else:
		print('Operação inválida! Digite apenas E, D ou S!')
