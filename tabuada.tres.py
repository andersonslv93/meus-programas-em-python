while True:
    print('-' * 30)
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('FIM DO PROGRAMA! Volte sempre.')
