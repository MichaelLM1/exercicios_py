cont = maior18 = 0
while cont < 5:
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    cont += 1 
print(f'Ao todo, temos {maior18} pessoas com mais de 18 anos')
