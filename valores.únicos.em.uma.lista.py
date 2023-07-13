lista = []
while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        print('Valor adicionado com sucesso...')
        c = str(input('Quer continuar? [S/N]')).strip().upper()
        lista.append(v)
    else:
        print('Valor duplicado! Não vou adicionar...')
        c = str(input('Quer continuar? [S/N]')).strip().upper()
    if c == 'N':
        lista.sort()
        break
print(f'Você digitou os valores {lista}')
        
