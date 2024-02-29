lista = []
for list in range(6):
    list = float(input())
    if list > 0:
        lista.append(list)
media = (sum(lista)) / len(lista)
print(f'{len(lista)} valores positivos')
print(f'{media:.1f}')

#Outra forma#
'''
soma = 0
quant = 0

for i in range(6):
    valor = float(input())
    soma = soma + valor
    quant += 1

print(f'{quant} valores positivos')
print(f'{soma / quant :0.1f}')

'''