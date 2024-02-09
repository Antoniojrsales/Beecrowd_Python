#Beecrowd 1050#
salario = float(input())
isento = 2000
imposto = 0

if salario <= isento:
    print('Isento')
else:
    if salario <= 3000:
        imposto += ((salario - 2000) * 8) / 100 #Calculando o percentual de 8% a cima da isencao Do Imposto#
    elif salario <= 4500:
        imposto += (1000 * 8) / 100 #Fatiando o percentual de 8% a cima da isencao Do Imposto#
        imposto += ((salario - 3000) * 18) /100 #Calculando o percentual de 18% a cima da isencao Do Imposto#
    else:
        imposto += (1000 * 8) / 100 #Fatiando o percentual de 8% a cima da isencao Do Imposto#
        imposto += (1500 * 18) / 100 #Fatiando o percentual de 18% a cima da isencao Do Imposto#
        imposto += ((salario - 4500) * 28) /100 #Calculando o percentual de 28% a cima da isencao Do Imposto#
    print(f'R$ {imposto:.2f}')
