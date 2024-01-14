compra = input().split()
A = int(compra[0])
B = int(compra[1])
lista_precos = {
    'Cachorro_quente': 4,
    'X_Salada': 4.5,
    'X_Bacon': 5,
    'Torrada_Simples': 2,
    'Refrigerante': 1.5,
}
if A == 1:
    total = lista_precos['Cachorro_quente'] * B
    print(f'Total: R$ {total:.2f}')
elif A == 2:
    total = lista_precos['X_Salada'] * B
    print(f'Total: R$ {total:.2f}')
elif A == 3:
    total = lista_precos['X_Bacon'] * B
    print(f'Total: R$ {total:.2f}')
elif A == 4:
    total = lista_precos['Torrada_Simples'] * B
    print(f'Total: R$ {total:.2f}')
elif A == 5:
    total = lista_precos['Refrigerante'] * B
    print(f'Total: R$ {total:.2f}')