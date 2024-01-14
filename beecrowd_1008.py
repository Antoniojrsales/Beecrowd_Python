NUMBER = int(input('Digite o Id do Funcionario: '))
HR = int(input('Digite quantas HRS trabalhadas: '))
VHR = float(input('Digite o valor da HR trabalhada: '))
SALARY = HR*VHR
print(f'NUMBER = {NUMBER}')
print(f'SALARY = U$ {SALARY:.2f}')
