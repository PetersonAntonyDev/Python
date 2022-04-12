import random

print('(x_x)===JOGO DA FORCA===(x_x)')
print('TEMA: 𓃭 𓃻 ANIMAIS 𓃻 𓃭')
lista = ['saguim', 'cachorro', 'peba', 'pombo', 'timbu', 'tiziu', 'teju', 'guaru', 'hiena', 'piaba']
animal = random.choice(lista)
digitados = []
chances = 10
print('-_' * 30)
while True:
    caractere = str(input('Digite uma letra: '))
    if len(caractere) > 1:
        print('!!!ERRO!!!')
        print('ATENÇÃO: VOCÊ SÓ PODE DIGITAR UMA LETRA POR VEZ')
        continue
    digitados.append(caractere)
    palavra_temporária = ''
    for letra_secreta in animal:
        if letra_secreta in digitados:
            palavra_temporária += letra_secreta
        else:
            palavra_temporária += '_'
    if palavra_temporária == animal:
        print('PARABÉNS!')
        print('Você livrou seu boneco da forca!')
        print('\U0001f44f', '\U0001f44f', '\U0001f44f', '\U0001f44f')
        break
    else:
        print(f'A palavra está assim, por enquanto: {palavra_temporária}')
    if caractere not in animal:
        chances -= 1
    if chances <= 0:
        print('!Você enforcou seu boneco!')
        print('(╥﹏╥)  (╥﹏╥)  (╥﹏╥)  (╥﹏╥)')
        break
    print(f'Você ainda tem {chances} chances')
    print()
print('A palavra certa era: ', animal)
