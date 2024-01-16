A, B= map(int, input().split())
tempo = 24
if A == B:
    print(f'O JOGO DUROU {tempo} HORA(S)')
elif A < B:
    print(f'O JOGO DUROU {B - A} HORA(S)')
elif A > B:
    print(f'O JOGO DUROU {(tempo - A) + (B)} HORA(S)')

#Forma melhorada#
'''inicio, fim = map(int, input().split())

tempo = fim - inicio

if tempo <= 0:
    tempo += 24

print(f'O JOGO DUROU {tempo} HORA(S)')'''
