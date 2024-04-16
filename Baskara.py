import math

def calcula_delta(a, b, c):
    delta = (b**2) - (4*a*c)
    return delta

def calcula_raizes(a, delta):
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    return raiz1, raiz2

a = float(input("Digite o valor de A: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = calcula_delta(a, b, c)

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui apenas uma raiz real: x = {raiz}")
    else:
        raiz1, raiz2 = calcula_raizes(a, delta)
        print(f"A equação possui duas raízes reais:\nx1 = {raiz1}\nx2 = {raiz2}")