# Conersao de entrada de dados
#ex:Calculo de bonus por tempo de serviço

anos = int(input('Anos de serviço: '))
valor_por_ano = float(input('Valor por ano: '))
bonus = anos*valor_por_ano
print('Bônus de R$ %-5.2f'% bonus)

