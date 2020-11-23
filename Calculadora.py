# Aluno: João Lucas De Souza Soares
#RA: N622DH-8
#Turma: CC2A30

#Faça um programa que receba dois números e mais o símbolo da operação (+, -, * e /) e realize o cálculo desses dois números. Uma calculadora:
#Cada operação deverá ser uma função diferente
#altere esse programa para que ele fique executando (pedindo os números) até que eu responda N para a pergunta "Deseja continuar (s/n)" 



def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2


cont = True
while cont:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    calculo = (input('Digite qual operação deseja realizar (+, -, * ou /): '))

    if calculo == '+':
        print('O resultado é {}'.format(soma(n1, n2)))
    elif calculo == '-':
        print('O resultado é {}'.format(subtracao(n1, n2)))
    elif calculo == '*':
        print('O resultado é {}'.format(multiplicacao(n1, n2)))
    elif calculo == '/':
        print('O resultado é {}'.format(divisao(n1, n2)))
    else:
        print('Operação inválida')

    opcao = input('eseja continuar [S,N]: ')
    if opcao.upper() == 'N':
        cont = False


    

