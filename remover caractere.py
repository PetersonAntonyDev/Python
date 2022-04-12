frase = str(input('Digite uma palavra ou uma frase: ')).lower()
caracte = str(input('Digite o carectere que deseja remover: ')).lower()
print('Frase/palavra sem o caractere que você digitou para remover:')
print(frase.replace(caracte, '*'))