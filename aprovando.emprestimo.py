casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))

prestaçao = casa / (anos * 12)

if prestaçao <= salario * 30 / 100:
    print('Para pagar uma casa de R${:.2f}, em {} anos, a prestação será de R${:.2f}.'.format(casa,anos,prestaçao))
    print('Emprestimo APROVADO!')
else:
    print('Para pagar uma casa de R${:.2f}, em {} anos, a prestação será de R${:.2f}.'.format(casa,anos,prestaçao))
    print('Emprestimo NÃO APROVADO!')
