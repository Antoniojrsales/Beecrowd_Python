'''Beecrowd 1047
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. 
A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .'''

hr_inicio, min_inicio, hr_fim,  min_fim = map(int, input().split())

min_inicio += hr_inicio * 60
min_fim += hr_fim * 60

tempo = min_fim - min_inicio

if tempo <= 0:
    tempo += 24 * 60

hora = tempo // 60
minuto = tempo % 60


print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
