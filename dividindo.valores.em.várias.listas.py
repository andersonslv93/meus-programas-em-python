lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? ')).strip().upper()
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()
    if c == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares e {pares}')
print(f'A lista de impares e {impares} ')
