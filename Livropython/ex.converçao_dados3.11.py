# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto .
# Exiba o valor de desconto e o preço a pagar.

preçoMerc = float(input('Informe o preço da mercadoria: '))
percent = float(input('Informe o percentual de desconto: '))
desconto = percent*preçoMerc
preçoPagar = preçoMerc-desconto
print('O valor do desconto %4.2f R$'%desconto)
print('O valor a pagar é de %5.2f R$'%preçoPagar)


