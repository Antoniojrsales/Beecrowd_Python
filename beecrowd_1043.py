A, B, C = map(float, input().split())
if (B - C) < A < B + C and (A - C) < B < A + C and (A - B) < C < A + B:
    print(f'Perimetro = {A + B + C}')
else:
    print(f'Area = {(A + B) * C / 2}') 