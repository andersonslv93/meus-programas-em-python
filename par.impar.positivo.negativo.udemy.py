num = int(input('Digite um numero: '))
p = num % 2

#processamento

if num >= 0 and p == 0:
    print('Par, positivo.')
    
elif num < 0 and p == 0:
    print('Par, negativo.')

elif num >= 0 and p == 1:
    print('Impart, positivo.')
else:
    print('Impar, negativo.')
