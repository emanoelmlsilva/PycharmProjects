notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x<7:
        notas[x] = float(input('Nota {}:'.format(x)))
        soma+=notas[x]
        x+=1
x=0
while x<7:
        print('Nota {}: {:.2f}'.format(x,notas[x]))
        x+=1
print('Media: {:.2f}'.format(soma/x))
