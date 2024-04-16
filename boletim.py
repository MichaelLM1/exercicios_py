# Indicando seu nome
print('='*20)
nome = input('digite seu nome: ').strip() .capitalize() .split()
print(f'Olá, {nome[0]}!')
print('='*20)

# Fazendo o login
print('Digite seu usuário e senha!')
while True:
    usuario = input('Usuário: ').strip() .capitalize()
    senha = input('Senha: ')
    if usuario == nome[0] and senha == '123':
        print('Bem vindo!')
        break
    else:
        print('Usuário ou senha incorretos!')

# Inserindo as notas e calculando a média
nota1 = float(input('nota do primeiro semestre:'))
nota2 = float(input('nota do primeiro semestre:'))
media = (nota1+nota2) / 2

# Verificando se o aluno passou de ano
print('sua média foi de:', media)
if media >= 7 and media <= 10:
    print('você está aprovado!')
elif media >= 5 and media < 7:
    print('você está de recuperação!')
elif media >= 0 and media < 5:
    print('você está reprovado!')
else:
    print(f'o valor {media} é invalido')