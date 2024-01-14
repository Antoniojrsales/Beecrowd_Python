N = float(input())
N += 0.0001
lista_notas = [100, 50, 20, 10, 5, 2]
lista_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in lista_notas:
    quantia_notas = int(N // nota)
    N -= quantia_notas * nota
    print(f"{quantia_notas} nota(s) de R$ {nota}.00")

print("MOEDAS:")
for moeda in lista_moedas:
    quantia_moedas = int(N // moeda)
    N -= quantia_moedas * moeda
    print(f"{quantia_moedas} moeda(s) de R$ {moeda:.2f}")