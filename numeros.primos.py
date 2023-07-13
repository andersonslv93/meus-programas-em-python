#numero primo só é divisivel por 1 e por ele mesmo
cont = 0
n = int(input('Digite um numero: '))
for c in range (1, n + 1):
    print(c, end= ' ')
    if n % c == 0:
        cont = cont + 1
print('\nO número {} foi divisível {} vezes.'.format(n,cont))        
if cont > 2:
    print('E por isso ele NÃO É PRIMO!')
elif cont == 2:
    print('E por isso ele É PRIMO!')
