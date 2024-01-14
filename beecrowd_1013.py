linha = input('Digite um valor (espaco) valor2 (espaco) valor3 (espaco): ').split()
A = int(linha[0])
B = int(linha[1])
C = int(linha[2])
if A == B and A == C and B == C:
    print('Deu empate')
elif A > B and A > C:
    print(f'{A} eh o maior')
elif B > A and B > C:
    print(f'{B} eh o maior')
else:
    print(f'{C} eh o maior')

#MAIOR_ABC = max(A,B,C)
#print(f'{MAIOR_ABC} eh o maior')

