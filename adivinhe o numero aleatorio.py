import random
tentativa1 = True
tentativa2 = 0
limitea = 10
limiteb = 20
numerogerado = random.randint(limitea, limiteb)
print('limite inferior é 10.')
print('limite superior é 20.')
while tentativa1:
    chute = int(input("Chute um número: "))
    if chute > numerogerado:
        numerogerado = random.randint(limitea, chute)
        chute = int(input("Chute um número: "))
        tentativa2 += 1
    if chute < numerogerado:
        numerogerado = random.randint(chute, random.randint(chute, chute + 15))
        chute = int(input("Chute um número: "))
        tentativa2 += 1
    if chute != numerogerado:
        tentativa2 += 1
    if chute == numerogerado:
        tentativa2 += 1
        print("Você acertou!")
        print("Você tentou " + str(tentativa2) + " vezes até acertar.")
        tentativa1 = False