maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O mais pesado tem {}kg.'.format(maior))
print('O mais leve tem {}kg.'.format(menor))
