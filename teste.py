meus_vetores = [0] * 7
totpar = 0
for i in range(7):
    meus_vetores[i] = int(input(f'Digite o {i + 1}o. valor: ')) 
    if meus_vetores[i] % 2 == 0:
        totpar += 1
print(f'O total de pares foi {totpar}')
for i in range(7):
    if meus_vetores[i] % 2 == 0:
        print(f'O valor Par na posicao {i}')


# Inicializa a lista e a contagem de números pares
meus_vetores = [int(input(f'Digite o {i + 1}o. valor: ')) for i in range(7)]
totpar = sum(1 for num in meus_vetores if num % 2 == 0)

# Exibe o total de números pares
print(f'O total de pares foi {totpar}')

# Exibe as posições dos números pares
for i, num in enumerate(meus_vetores):
    if num % 2 == 0:
        print(f'O valor Par na posicao {i}')