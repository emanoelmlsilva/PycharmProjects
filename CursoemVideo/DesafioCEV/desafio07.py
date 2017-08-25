#Desenvolva um programa que leia as duas notas de um aluno. calcule e mostra  a sua média.

nota1 = float(input('Digite a primeria nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1+nota2)/2
print('A media entre {} e {} é {}'.format(nota1,nota2,m))
