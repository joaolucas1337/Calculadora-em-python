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


    

