km = float(input('Informe a velocidade do carro: '))
multa = (7.00 * km) - (80 * 7)

if km <= 80:
    print('Dirija com cuidado.\nTenha um bom dia.')
else:
    print('MULTADO. Você ultrapassou o limite de velocidade. Deve pagar uma multa de {:.2f}R$!.'.format(multa))
