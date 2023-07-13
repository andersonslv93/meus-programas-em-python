#entrada

maior = 0

#processamento

n = int(input('Digite um número: '))

while n != 0:
    if n > maior:
        maior = n
    n = int(input('Digite um número: '))
print ('O maior número é {}.'.format(maior))