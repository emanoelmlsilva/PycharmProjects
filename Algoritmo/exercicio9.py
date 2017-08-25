"""Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente."""

nota1 = float(input('nota1: '))
nota2 = float(input('nota2: '))
nota3 = float(input('nota3: '))
media = (nota1*2+nota2*3+nota3*5)/10
print('Média Ponderada: %3.2f'%media)
