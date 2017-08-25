# Modifique o programa da listagem 5.10 para que aceite respostas com letras maiusculas e menusculas em todas as questoes

ponto = 0
questao = 1

while(questao <=3):

    resposta = input('Resposta da questão %d: '%questao)
    if(questao == 1 and resposta == 'b' or questao == 1 and resposta == 'B'):
        ponto += 1
    if(questao == 2 and resposta == 'a' or questao == 2 and resposta == 'A'):
        ponto += 1
    if(questao == 3 and resposta == 'd' or questao == 3 and resposta == 'D'):
        ponto += 1
    questao += 1
print('O aluno fez %d ponto(s)'%ponto)
