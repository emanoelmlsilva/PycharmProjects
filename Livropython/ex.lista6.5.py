ultimo = 10
fila  = list(range(1,ultimo+1))
while True:
	print('\nExistem {} clientes na fila'.format(len(fila)))
	print('Fila atual:',fila)
	print('Digite F para adicioar um cliente ao fim da fila',end=' ')
	print('ou A para realizar o atendimento. S para sair.')
	operaçao = input('Operação (F, A ou S):')
	cont = 0
	sair = False
	while cont < len(operaçao):
		if operaçao[cont] == 'A':
			if(len(fila))>0:
				atendido = fila.pop(0) #del fila[0]
				print('Cliente {} atendido'.format(atendido))
			else:
				print('Fila vazia! Ninguém para atender.')
		elif operaçao[cont] == 'F':
			ultimo+=1 #Incrementa o ticket do novo cliente
			fila.append(ultimo)
		elif operaçao[cont] == 'S':
			sair = True
			break
		else:
			print('Operação inválida! Digite apenas F, A ou S!')
		cont+=1
	if sair:
		break
