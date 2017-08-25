# Exemplo de composiçao de string

nome = 'jose'
idade = 22
grana = 51.34

print('%s tem %d anos e R$%f no bolso' %(nome, idade , grana))

print('%12s tem %3d anos e R$%5.2f no bolso'%(nome,idade,grana))

print('%8s tem %03d anos e R$%5.2f no bolso'%(nome,idade,grana))

print('%-12s tem %-3d anos e R$%-.2f no bolso'%(nome,idade,grana))
