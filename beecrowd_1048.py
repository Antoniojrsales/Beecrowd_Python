#Beecrowd 1048#

salario = float(input())
percentual = [15, 12, 10, 7, 4]

if salario <= 400:
    aumento = salario * (percentual[0] / 100)
    print(f'Novo salario: {salario + aumento:.2f}')
    print(f'Reajuste ganho: {aumento:.2f}')
    print(f'Em percentual: {percentual[0]} %')
elif salario <= 800:
    aumento = salario * (percentual[1] / 100)
    print(f'Novo salario: {salario + aumento:.2f}')
    print(f'Reajuste ganho: {aumento:.2f}')
    print(f'Em percentual: {percentual[1]} %')
elif salario <= 1200:
    aumento = salario * (percentual[2] / 100)
    print(f'Novo salario: {salario + aumento:.2f}')
    print(f'Reajuste ganho: {aumento:.2f}')
    print(f'Em percentual: {percentual[2]} %')
elif salario <= 2000:
    aumento = salario * (percentual[3] / 100)
    print(f'Novo salario: {salario + aumento:.2f}')
    print(f'Reajuste ganho: {aumento:.2f}')
    print(f'Em percentual: {percentual[3]} %')
else:
    aumento = salario * (percentual[4] / 100)
    print(f'Novo salario: {salario + aumento:.2f}')
    print(f'Reajuste ganho: {aumento:.2f}')
    print(f'Em percentual: {percentual[4]} %')

#Forma melhorada
'''salario_antigo = float(input())
percentual = 0

if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 10
else:
    percentual = 4

aumento = salario * (percentual / 100)
print(f'Novo salario: {salario + aumento:.2f}')
print(f'Reajuste ganho: {aumento:.2f}')
print(f'Em percentual: {percentual} %')'''


