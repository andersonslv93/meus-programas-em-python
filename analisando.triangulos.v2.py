r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('De acordo com essas retas, elas não formam um triangulo! ')
elif r1 == r2 and r1 == r3 and r2 == r1 and r2 == r3 and r3 == r1 and r3 == r2:
    print('Triangulo EQUILÁTERO.')
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r1 and r2 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2 or r3 == r2 and r3 != r1:
    print('Triangulo ISÓSCELES.')
elif r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r2 and r3 != r1:
    print('Triangulo ESCALENO.')
