horas_trabalhadas = float(input('Total de horas trabalhadas: '))
salario = horas_trabalhadas * 10.00

if horas_trabalhadas >= 50:
    excesso = horas_trabalhadas - 50
    extra = excesso * 20
    total = 50 * 10 + extra
    print('Salario total: R${:.2f} \nExtra: R${:.2f}'.format(total,extra))
else:
    horas_trabalhadas < 50
    total = horas_trabalhadas * 10
    print('Salario total: R${:.2f} \nExtra: R$0'.format(total))
