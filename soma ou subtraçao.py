import random

n = 0
n1 = 0
operador = ""
acertos = 0
tentativas = 4
resultado = 0
teste = ""

def gerador():
    global n, n1, operador, resultado
    n = random.randint(1, 30)
    n1 = random.randint(1, 30)
    operador = random.choice("+" + "-")
    if operador == "+":
        resultado = n + n1
    else:
        resultado = n - n1

while True:
    gerador()
    print('Você só tem ', str(tentativas), 'chances.')
    chute = int(input('Qual é o resultado da operação: ' + str(n) + operador + str(n1) + '? '))

    if chute == resultado:
        print('Você acertou!')
        acertos += 1
        print('Você já acertou ', str(acertos),  'vezes.')
        if (acertos == 10):
            break
        gerador()
    else:
        print('Errado!')
        tentativas = tentativas - 1
        if (tentativas == 0):
            print('Você perdeu todas chances!')
            break