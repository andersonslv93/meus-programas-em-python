salario = float(input('Qual é o salário do funcionário? '))

# 15% 
if salario <= 1250.00:
    quinze = salario * 15 / 100
    total1 = salario + quinze
    print('Ganhou aumeno de 15%, seu salario de {:.2f}R$ passa a ser {:.2f}R$.'.format(salario,total1))
    
# 10%
if salario > 1250.00:
    dez = salario * 10 / 100
    total2 = salario + dez
    print('Ganhou aumento de 10%, seu salario de {:.2f}R$ passa a ser {:.2f}R$.'.format(salario,total2))
