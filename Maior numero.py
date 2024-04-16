n1 = int(input('digite o primeiro numero: ')) 
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if n1 >= n2 and n1 >= n3:
    print('o numero', n1,'é o maior')
elif n2 >= n1 and n2 >= n3:
    print('o numero', n2, 'é o maior')
else:
    print('o numero', n3, 'é o maior')
    