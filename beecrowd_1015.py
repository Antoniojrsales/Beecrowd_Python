import math
x1, y1 = input('Digite o x1 (espaco) y1 (espaco) :').split()
x2, y2 = input('Digite o x2 (espaco) y2 (espaco): ').split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
resultado = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
print(f'A distancia entre os pontos sera de {resultado:.4f}')