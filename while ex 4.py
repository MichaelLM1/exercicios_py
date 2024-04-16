while True:
    numero = int(input('Digite um número: '))
    if numero >=1 and numero <= 10:
        break
    print('Número inválido! Por favor, digite um número entre 1 e 10.')
for c in range(1, 11):
    print(f'{numero} X {c} = {numero * c }')
        
