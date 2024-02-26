#Beecrowd#
dia_inicio = int(input('').split()[1])
hr_inicio, min_inicio, seg_inicio = map(int, input().split(':'))
t1 = seg_inicio + min_inicio * 60 + hr_inicio * 60 * 60 + dia_inicio * 24 * 60 * 60

dia_fim = int(input('').split()[1])
hr_fim, min_fim, seg_fim  = map(int, input(). split(':'))
t2 = seg_fim + min_fim * 60 + hr_fim * 60 * 60 + dia_fim * 24 * 60 * 60

dif = t2 - t1
w = dif // (24 * 60 * 60)
dif = dif % (24 * 60 * 60)

x = dif // (60 * 60)
dif = dif % (60 * 60)

y = dif // (60)
dif = dif % (60)

z = dif 

print(f'{w} dia(s)')
print(f'{x} hora(s)')
print(f'{y} minuto(s)')
print(f'{z} segundo(s)')
