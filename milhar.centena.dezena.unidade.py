num = int(input('Digite um numero: '))
n = str(num)

if n[3:]:
    unidade = n[3]
    dezena = n[2]
    centena = n[1]
    milhar = n[0]
    print(' Analisando o numero {}\n Unidade: {}\n Dezena: {} \n Centena: {}\n Milhar: {}'.format(n, unidade, dezena, centena, milhar))
    
elif n[2:]:    
    unidade = n[2]
    dezena = n[1]
    centena = n[0]
    milhar = 0
    print(' Analisando o numero {}\n Unidade: {}\n Dezena: {} \n Centena: {}\n Milhar: {}'.format(n, unidade, dezena, centena, milhar))

elif n[1:]:
    unidade = n[1]
    dezena = n[0]
    centena = 0
    milhar = 0
    print(' Analisando o numero {}\n Unidade: {}\n Dezena: {} \n Centena: {}\n Milhar: {}'.format(n, unidade, dezena, centena, milhar))

elif n[0]:
    unidade = n[0]
    dezena = 0
    centena = 0
    milhar = 0
    print(' Analisando o numero {}\n Unidade: {}\n Dezena: {} \n Centena: {}\n Milhar: {}'.format(n, unidade, dezena, centena, milhar))
    
´=
