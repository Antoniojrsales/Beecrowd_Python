valores = list(map(int, input().split()))
sorteados = sorted(valores, key=int)

for sort in sorteados:
    print(sort)

print()

for i in valores:
    print(i)