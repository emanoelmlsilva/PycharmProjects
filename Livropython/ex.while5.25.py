"""Escreva um programa que calcule a raiz quadrada de um número.Utilize o método de Newton para
obter um resultado aproximado.Sendo n o número a obter a raiz quadrada, considere a base b=2.Calcule
p usando a fórmula p = (b+(n/b))/2.Agora,calcule o quadrado de p.A cada passo,faça b=p e recalcule
p usando a fórmula apresentada.Pare quando a difrença absoluta entre n e o quadrado de p for menor
que 0.0001."""
num = int(input('informe o valor que deseja saber a raiz quadrada no motodo de newton: '))
while num != 0.0001:
    b = num / 2
    