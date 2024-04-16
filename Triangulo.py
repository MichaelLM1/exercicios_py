l1 = int(input('Digite o tamanho do primeiro lado: '))
l2 = int(input('Digite o tamanho do segundo lado: '))
l3 = int(input('Digite o tamanho do terceiro lado: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3:
        print ('Triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print ('Triângulo Isósceles')
    else:
        print ('Triângulo Escaleno')
else:
    print ('os lados nao formam um triangulo')