lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letra = str(input('Digite uma letra: '))
letra2 = str(input('Digite a segunda letra: '))
def buscarletra (lista, pesquisa):
    for a in range(len(lista)):
        if(lista[a]) == pesquisa:
            return a
    return -1
while True:
    try:
        resultado = buscarletra(lista, letra)
        if (resultado != -1):
            print(letra, 'está no índice', str(resultado))

        resultado2 = buscarletra(lista, letra2)
        if (resultado2 != -1):
            print(letra2, 'está no índice', str(resultado2))
            break
    except:
        print('ERRO!')
a = (buscarletra(lista, letra) - buscarletra(lista, letra2)) * (-1)
if a > 0:
    print('O número de caracteres entre eles é:', a)
else:
    print('ERRO!!')
    print('Para funcionar, digite as letras em ordem alfabética.')