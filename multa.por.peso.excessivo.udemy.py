peso_peixe = float(input('Digite o peso de peixes: '))

if peso_peixe <= 50.00:
    print('Não houve excesso, portanto, não haverá multa.')
else:
    peso_peixe > 50.00
    excesso = peso_peixe - 50.00
    multa = excesso * 4.00
    print('Você ultrapassou o excesso permitido por lei, com {:.2f}Kg de peixe, e com excesso de {:.2f}kg a mais, portanto, sua multa será de {:.2f}R$.'.format(peso_peixe, excesso, multa))
