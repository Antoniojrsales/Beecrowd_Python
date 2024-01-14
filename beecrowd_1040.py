notas = input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4) / 10
print(f'Media: {media:.1f}')
if media > 7:
    print('Aluno aprovado.')
elif media >= 5 and media < 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    media_final = (nota_exame + media) / 2
    if media_final >= 5:
        print(f'Nota do exame: {nota_exame:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print('Aluno reprovado.')
elif media < 5:
    print('Aluno reprovado.')