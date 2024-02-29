#Beecrowd 1065

result = []
for list in range(5):
    if float(input()) % 2 == 0:
        result.append(list)
print(f'{len(result)} valores pares')