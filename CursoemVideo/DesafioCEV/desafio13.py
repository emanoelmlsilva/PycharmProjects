#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input('Digite o salario do funcionario: '))
newsal = salario + salario * 0.15
print('O novo salario é de {:.2f}'.format(newsal))
