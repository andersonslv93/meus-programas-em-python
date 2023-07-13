preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção: '))

dez = preço * 10 / 100
dez_desconto = preço - dez
cinco = preço * 5 / 100
cinco_desconto = preço - cinco
juross = preço * 20 / 100
juros = preço + juross
duas = preço / 2

if opçao == 1:
    print('Sua compra de R${:.2f}, sairá a R${:.2f}, com 10% de desconto. Bela economia.'.format(preço, dez_desconto))
elif opçao == 2:
    print('Sua compra de R${:.2f}, sairá a R${:.2f}, com 5% de desconto.'.format(preço,cinco_desconto))
elif opçao == 3:
    print('Sua compra de R${:.2f} sairá em 2x de R${:.2f}.'.format(preço,duas))
elif opçao == 4:
    parcela = int(input('Quantas vezes deseja parcelar? '))
    valor_parcela = juros / parcela
    print('Sua compra de R${:.2f}, com um juros de 20%, sairá a R${:.2f} no total {} parcelas de R${:.2f} por mês.'.format(preço, juros, parcela, valor_parcela))

