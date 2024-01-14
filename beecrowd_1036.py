from math import sqrt
linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

delta = B ** 2 - 4 * A * C

try:
    R1 = (-B + sqrt(delta)) / (2 * A)
    R2 = (-B - sqrt(delta)) / (2 * A)

    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
except ValueError:
    print('Impossivel calcular')
except ZeroDivisionError:
    print('Impossivel calcular')


