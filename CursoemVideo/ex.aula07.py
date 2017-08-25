#nome = str(input('Qual o seu nome?'))
#print('Prazer em conhecer  {:20}!'.format(nome))#colocando nome em 20 estapaços
#print('Prazer em conhecer  {:>20}!'.format(nome))#colocando nome em 20 estapaços a direita
#print('Prazer em conhecer  {:<20}!'.format(nome))#colocando nome em 20 estapaços a esquerda
#print('Prazer em conhecer  {:^20}!'.format(nome))#centraliza o nome
#print('Prazer em conhecer  {:=^20}!'.format(nome))#centraliza o nome com iguais em volta ou qualque outro simbolo

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sb = n1 - n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('A soma é {}, o produto é {}, subtraçao é {} e a divisao é {:.2f}'.format(s,m,sb,d),end =' ')#serve para evitar quebra a linha e \n para quebrar
print('Divisao inteira é {}, potênciacao é {} e o resto da divisao é {}'.format(di,e,r))