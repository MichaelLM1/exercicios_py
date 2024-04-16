dias28 = '02'
dias30 = '04', '06', '09', '11'
dias31 = '01', '03', '05', '07', '08', '10', '12'

numdias = int(input('digite um número e veja qual mês possui essa quantidade de dias: '))
if numdias == 28:
    print(f'O mês que tem {numdias} dia é o mês {dias28}')
elif numdias == 30:
    print(f'Os meses que tem {numdias} dias são os meses {dias30}')
elif numdias == 31:
    print(f'Os meses que tem {numdias} dias são os meses {dias31}')
else:
    print(f'Não existe nenhum mês com {numdias} dias!')