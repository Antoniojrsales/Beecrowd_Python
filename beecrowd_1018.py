nota001 = int(input())
print(nota001)

nota100 = nota001//100
nota001 = nota001%100

nota050 = nota001//50
nota001 = nota001%50

nota020 = nota001//20
nota001 = nota001%20

nota010 = nota001//10
nota001 = nota001%10

nota005 = nota001//5
nota001 = nota001%5

nota002 = nota001//2
nota001 = nota001%2

print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota050} nota(s) de R$ 50,00')
print(f'{nota020} nota(s) de R$ 20,00')
print(f'{nota010} nota(s) de R$ 10,00')
print(f'{nota005} nota(s) de R$ 5,00')
print(f'{nota002} nota(s) de R$ 2,00')
print(f'{nota001} nota(s) de R$ 1,00')


'''Outra forma com loop
notas = int(input())

lista_notas=[100, 50, 20, 10, 5, 1]

for nota in lista_notas:
    qtd_notas = notas // nota
    notas -= qtd_notas * nota
    print(f"{qtd_notas} nota(s) de R$ {nota}")'''


