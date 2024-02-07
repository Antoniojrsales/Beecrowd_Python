#Beecrowd 1050#

ddd = int(input())
lista_ddd = [
    {'DDD': '61', 'Destino': 'Brasilia'},
    {'DDD': '71', 'Destino': 'Salvador'},
    {'DDD': '11', 'Destino': 'Sao Paulo'},
    {'DDD': '21', 'Destino': 'Rio de Janeiro'},
    {'DDD': '32', 'Destino': 'Juiz de Fora'},
    {'DDD': '19', 'Destino': 'Campinas'},
    {'DDD': '27', 'Destino': 'Vitoria'},
    {'DDD': '31', 'Destino': 'Belo Horizonte'},
]

if ddd == 61:
    print(lista_ddd[0]['Destino'])
elif ddd == 71:
    print(lista_ddd[1]['Destino'])
elif ddd == 11:
    print(lista_ddd[2]['Destino'])
elif ddd == 21:
    print(lista_ddd[3]['Destino'])
elif ddd == 32:
    print(lista_ddd[4]['Destino'])
elif ddd == 19:
    print(lista_ddd[5]['Destino'])
elif ddd == 27:
    print(lista_ddd[6]['Destino'])
elif ddd == 31:
    print(lista_ddd[7]['Destino'])
else:
    print('DDD nao cadastrado')

