valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 745
apagar=valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print('%d cédula(s) de R$%d'%(cedulas,atual))
        if apagar == 0:
            break
        if atual == 745:
            atual = 501
        elif atual == 501:
            atual = 384
        elif atual == 384:
            atual = 100
        elif atual == 100:
            atual = 7
        elif atual == 7:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0