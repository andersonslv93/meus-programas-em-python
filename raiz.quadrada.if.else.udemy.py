n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
n4 = int(input('Quarto numero: '))

q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 >= 1000:
    print('{}'.format(q3))
    
else: 
    print('{},{},{},{}'.format(q1,q2,q3,q4))
