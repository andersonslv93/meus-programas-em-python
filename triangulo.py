r1 = float(input('Digie a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima FORMAM um triangulo.'
else:
    print('Os seguimentos acima NÃO FORMAM um triangulo.')
