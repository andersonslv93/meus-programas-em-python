print('-' * 30)
print('     LOJA SUPER BARATÃO')
print('-' * 30)
caro = 0
menor = 0
total = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont +=1
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    total += preço
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if c == 'N':
        break
print('O total da compra foi R${:.2f}.'.format(total))
print('Temos {} produtos custando mais de R$1000.00.'.format(caro))
print('O produto mais barato foi {} que custa R${:.2f}.'.format(barato, menor))
