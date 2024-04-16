n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
print('qual operação você quer fazer?\n[ + ] ADIÇÃO\n[ - ] SUBTRAÇÃO\n[ * ] MULTIPLICAÇÃO\n[ / ] DIVISÃO')

while True:
    operação = input('OPÇÃO: ')
    if operação == '+':
        print(f'{n1} + {n2} = {n1 + n2}')
        break
    elif operação == '-':
        print(f'{n1} - {n2} = {n1 - n2}')
        break
    elif operação == '*':
        print(f'{n1} X {n2} = {n1 * n2}')
        break
    elif operação == '/':
        print(f'{n1} / {n2} = {n1 / n2}')
        break
    else:
        print('operador invalido!')
