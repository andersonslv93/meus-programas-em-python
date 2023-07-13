lista = ('Lápis','1.75','Borracha','2.00','Caderno','15.90','Estojo','25.00',
         'Transferidor','4.20','Compasso','9.99','Mochila','120.32','Canetas',
         '22,30','Livro','32.90')

print('-' * 40)
print('             LISTAGEM DE PREÇOS')
print('-' * 40)

for l in range(0,len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]}..................', end=' ')
    else:
        print(f'R${lista[l]}')
print('-' * 40)
