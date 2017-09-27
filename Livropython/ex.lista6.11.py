l=[]
while True: #não tem como usar for por não ter um tamanho definido.
        n = int(input('Digite um número (0 sai): '))
        if n==0:
                break
        l.append(n)

for x in l:
        print(x,end=' ')
print()


