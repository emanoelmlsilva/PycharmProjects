"""n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
s = n1 + n2
print(type(n2))#saber qual o tipo da variavel
print('a soma entre {0} e {1} vale {2}'.format(n1,n2,s))#nova sintax"""

algo = input('Digite algo: ')
print('Tipo: {}'.format(type(algo)))
print('Número {}'.format(algo.isnumeric()))
print('Alphabetico ',algo.isalpha())
print('AlphaNumerico {}'.format(algo.isalnum()))
