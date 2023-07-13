altura = float(input('Digite sua altura: '))
sexo = str(input('Digite seu sexo: '))
ideal_homem = (72.7 * altura) - 58
ideal_mulher = (62.1 * altura) - 44.7

#if, else

if sexo == 'm' or sexo == 'M':
    print('O peso ideal para este homem é de {:.2f}KG.'.format(ideal_homem))
elif sexo == 'f' or sexo == 'F': 
    print('O peso ideal para esta mulher e de {:.2f}KG.'.format(ideal_mulher))
else:
    print('Sexo não definido, digite corretamente.')
