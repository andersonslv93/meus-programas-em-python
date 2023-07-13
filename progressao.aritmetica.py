print('=' * 22)
print(' 10 TERMOS DE UMA PA     ')
print('=' * 22)

t1 = int(input('Primeiro Termo: '))
r1 = int(input('Razão: '))
termo = t1 + (10 - 1) * r1
for c in range(t1, termo + r1, r1):
    print(c ,'->', end = ' ')
print('ACABOU!')
