salario = float(input('Qual é o salário do funcionário?'))
aumento = salario * 15 / 100
aumento2 = salario + aumento
print('O funcionário que ganhava {:.2f}R$, com 15% de aumento, agora passa a ganhar {:.2f}R$.'.format(salario, aumento2))
