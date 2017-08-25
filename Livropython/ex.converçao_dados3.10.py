# Faça um programa que calcule o aumento de um salario.
# Ele deve solicitar o valor do salario e a porcentagem do aumento .
# Exiba o valor do aumento e do novo salario

salario = float(input('Entre com o salario: '))
porcentagem = float(input('Informe a porcentagem: '))
aumento = salario * porcentagem
novoSal = aumento + salario
print('Valor do aumento %5.2f R$'%aumento)
print('Valor do novo salario %4.2f R$'%novoSal)