mes = 'mes', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
while True:
    n1 = int(input('digite um número entre 1 e 12: '))
    if n1 >= 1 and n1 <= 12:
        print(f'O número {n1} corresponde ao mês de {mes[n1]}')
        break
    else:
        print('Número inválido!')