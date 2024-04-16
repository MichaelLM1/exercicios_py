codigo = int(input('digite o código: '))
quantidade = int(input('digite a quantidade: '))

if codigo == 100:
    print(f'O Cachorro Quente custa R${1.20 * quantidade:.2f}')
elif codigo == 101:
    print(f'O Bauru Simples custa R${1.30 * quantidade:.2f}')
elif codigo == 102:
    print(f'O Bauru com Ovo custa R${1.50 * quantidade:.2f}')
elif codigo == 103:
    print(f'O Hamburger custa R${1.20 * quantidade:.2f}')
elif codigo == 104:
    print(f'O Cheeseburger custa R${1.70 * quantidade:.2f}')
elif codigo == 105:
    print(f'O Suco custa R${2.20 * quantidade:.2f}')
elif codigo == 106:
    print(f'O Refrigerante custa R${1.00 * quantidade:.2f}')
else:
    print('Produto não encontrado')
