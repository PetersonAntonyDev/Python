palavras = list()
print('Digite "Fim" para encerra sua lista de 10 pessoas (Digite as palavras individual): ')
while True:
    frases = str(input('Digite os nomes das pessoas: '))
    if frases == 'Fim':
        break
    palavra = frases.split()
    for word in palavra:
        if word not in palavras:
            palavras.append(word)
palavras.sort()
print('Lista em ordem alfabética:', palavras)