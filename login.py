login = str(input('Defina seu E-mail: '))
senha = str(input('Defina sua senha: '))
print('Você está cadastrado!')
print('Faça seu login para entrar.')
log = str(input('Login: '))
sen = str(input('Senha: '))

for c in (4, 0, 1):
    if log == login and sen == senha:
        print('Carregando...')
        print('Bem-vindo!')
        break
    else:
        print('Usúario ou senha incorreto')
    log = str(input('Login: '))
    sen = str(input('Senha: '))
    continue
else:
    print('Bloqueado!')

