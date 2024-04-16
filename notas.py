while True:
    nota = int(input('Digite a nota: '))
    if nota >= 86 and nota <= 100:
        conceito = 'A'
        break
    elif nota >= 61 and nota < 86:
        conceito = 'B'
        break
    elif nota >= 36 and nota < 60:
        conceito = 'C'
        break
    elif nota >= 1 and nota < 36:
        conceito = 'D'
        break
    elif nota == 0:
        conceito = 'E'
        break
    else:
        print('Nota invalida')
print(f'A nota {nota} equivale a → {conceito}')