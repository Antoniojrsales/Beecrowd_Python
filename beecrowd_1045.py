valores = list(map(float, input().split()))
sorteados = sorted(valores)
A = sorteados[-1]
B = sorteados[-2]
C = sorteados[-3]

if A < B + C:
    if A ** 2 == B ** 2 + C ** 2:
        print('TRIANGULO RETANGULO')
    elif A ** 2 > B ** 2 + C ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif A ** 2 < B ** 2 + C ** 2:
        print('TRIANGULO ACUTANGULO')

    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')

else:
    print('NAO FORMA TRIANGULO')

