#Beecrowd 1060#
'''a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
lista = [a, b, c, d, e, f]'''
result = []
for list in range(6):
    if float(input()) > 0:
        result.append(list)
print(f'{len(result)} valores positivos')
        