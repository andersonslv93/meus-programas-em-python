n1 = int(input('Digie o primeiro valor: '))
n2 = int(input('Digie o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

#menor numero
if n1 < n2 and n1 < n3:
    print('O menor número é {}.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é {}.'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O menor número é {}.'.format(n3))

#maior numero
if n1 > n2 and n1 > n3:
    print('O maior número é {}.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}.'.format(n2))
else:
    print('O maior número é {}.'.format(n3))
