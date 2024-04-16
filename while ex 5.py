senha = 1234
while True:
    tentativa = int(input('Digite a senha: '))
    if tentativa == senha:
        print('Senha correta!')
        break
    print('Senha incorreta! Tente novamente...')
    
