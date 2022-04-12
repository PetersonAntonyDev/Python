print('Quando terminar a compra do cliente, digite "pronto" ')
produtos = []
valor = 0

while True:
    produto = input('Nome do produto: ')
    if produto == 'pronto':
        print('valor apurado até o momento: R$ {:.2f}'.format(valor))
        finalizar = input('você deseja finalizar o caixa "sim" ou "não"? ')
        if finalizar == 'sim':
            break
        else:
            continue
    valor += float(input('Digite o valor do produto: R$'))
    produtos.append(produto)
print('Valor apurado no dia: R$ {:.2f}'.format(valor))
print('lista dos produtos vendidos no dia:')
print(produtos)

