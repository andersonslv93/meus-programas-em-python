produto = float(input('Digite o valor do produto:'))
desconto = produto * 5 / 100
desconto2 = produto - desconto
print('O produto que custava {:.2f}R$, com o desconto de 5%, ficará {:.2f}R$.'.format(produto, desconto2))
