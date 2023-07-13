km = float(input('Qual a distância da sua viagem ? '))

if km <= 200.00:
    valor = km * 0.50
    print('Você está prestes a começar uma viagem de {:.1f}KM.'.format(km))
    print('O preço da sua viagem será de {:.2f}R$.'.format(valor))
else:
    valor_promocional = km * 0.45
    print('Você está prestes a começar uma viagem de {:.1f}KM.'.format(km))
    print('O preço da sua viagem será de {:.2f}R$.'.format(valor_promocional))
