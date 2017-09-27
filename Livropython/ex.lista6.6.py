ultimoa = 10
ultimob = 10
fila  = list(range(1,ultimoa+1))
filb  = list(range(1,ultimob+1))
while True:
	print('\nExistem {} clientes na fila'.format(len(fila)))
	print('Fila atual:',fila)
	print('Digite F para adicioar um cliente ao fim da fila',end=' ')
	print('ou A para realizar o atendimento. S para sair.')
	operaçao = input('Operação (F, A ou S):')
	if operaçao == 'S':
		break
	print('A para atendimento da fila 1 e B para atendimento para fila 2')
	atend = input('atendimento (A ou B): ')
	print('para chegada de clientes F para fila 1 e G para fila 2')
	chegada = input('chegada (F ou G): ')
	cont = 0
	sair = False
	while cont < len(operaçao):
		if operaçao[cont] == 'A':
			if atend == 'A' and len(fila)>0:
				atendidoa = fila.pop(0) #del fila[0]
				print('Cliente {} atendido na fila 1'.format(atendidoa))
			elif atend == 'B' and len(filb)>0:
				atendidob = filb.pop(0)
				print('Cliente {} atendido na fila 2'.format(atendidob))
			else:
				print('Fila vazia! Ninguém para atender na fila 1 ou fila 2.')
		elif operaçao[cont] == 'F':
			if chegada == 'F':
				ultimoa+=1 #Incrementa o ticket do novo cliente
				fila.append(ultimoa)
				print('Cliente {} foi adicionado na fila 1'.format(ultimoa))
			elif chegada == 'G':
				ultimob+=1 #Incrementoa o ticket do novo cliente
				filb.append(ultimob)
				print('Cliente {} foi adicionado na fila 2'.format(ultimob))
			else:
				print('Não à mais clientes')
		elif operaçao[cont] == 'S':
			sair = True
			break
		else:
                	print('Operação inválida! Digite apenas F, A ou S!')
		cont+=1
	if sair:
        	break
