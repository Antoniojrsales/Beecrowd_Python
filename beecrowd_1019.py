segundo = int(input())

hora = segundo//3600
segundo = segundo%3600

minuto = segundo//60
segundo = segundo%60

print(f'{hora}:{minuto}:{segundo}')
