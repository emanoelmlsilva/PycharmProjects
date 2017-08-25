valor = float(input('Digite o valor a pagar: '))
cedulas = 0
atual = 745
apagar=valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print('{} cédula(s) de {}R$'.format(cedulas,atual))
        else:
            print('{} moedas(s) de {:.2f}R$'.format(cedulas, atual))
        if apagar == 0.00:
            break
        elif atual == 745:
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
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        elif atual == 0.01:
            atual = 0.00
        cedulas = 0

