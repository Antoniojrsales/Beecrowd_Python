linha = input('Digite um valor1 (espaco) valor2 (espaco) valor3 (espaco): ').split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])
pi = 3.14159
triangulo = A * C / 2
circulo = pi * C ** 2
trapezio = (A + B)* C /2
quadrado = B * B
retangulo = A * B
print(f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\
    \nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}')
