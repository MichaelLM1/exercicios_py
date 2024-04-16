print('insira um número de 1 a 10 e veja sua tabuada!')
print('-=-'*10)

while True:
    numero = int(input('número: '))
    if numero >= 1 and numero <= 10:
        for c in range(1, 11):
            print(f'{numero} X {c} = {numero * c}')
        break
    else:
        print('Número inválido')
    