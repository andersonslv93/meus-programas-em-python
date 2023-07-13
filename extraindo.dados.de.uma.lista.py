lista = []
cont = 0
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    cont += 1
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    if c == 'N':
        lista.sort(reverse=True)
        break
print('-=' * 40)
print(f'Os valores em ordem decrescente são {lista}')
print(f'Você digitou {cont} elementos.')

if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 faz parte da lista')
