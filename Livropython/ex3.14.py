#Exemplo de fatiamento com omissao de valores e com indices negativos

s = 'ABCDEFGHI'
print(s[:2]) #indica do inicio até o segundo carctere(sem utilizalo)

print(s[1:])#indica do caractere de posiçao 1 ate o final da string

#Utilizando valores negativos para indicar posiçoes a partir da direita(ex: -1 último,-2 penúltimo caractere

print(s[0:-2])

print(s[:])

print(s[-1:])

print(s[-5:7])

print(s[-2:-1])