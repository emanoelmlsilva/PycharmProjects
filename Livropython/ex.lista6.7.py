p = input('Digite os parenteses: ')
cont = 0
inv = 0
s=0
while cont < len(p):
        if p[cont] == '(' and p[inv] == ')':
                s+=2
        else:
                s-=1
                break

        cont+=1
if s % 2 ==  0:
        print('OK')
else:
        print('ERRO')

""" resposta do livro
expressao = input('paratenses: ')
pilha = []
x = 0
while x < len(expressao):
	if expressao[x] == '(':
		pilha.append('(')
	if expressao[x] == ')':
		if len(pilha)>0:
			del pilha[-1]	#topo = pilha.pop(-1)
		else:
			pilha.append(')')
			break
	x+=1
if len(pilha)==0:
	print('OK')
else:
	print('ERRO')"""

