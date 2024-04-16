letra = input('digite uma letra: ').strip() .lower()[0]
if letra in 'aeiou':
    print('É uma vogal!')
else:
    print('É uma consoante!')