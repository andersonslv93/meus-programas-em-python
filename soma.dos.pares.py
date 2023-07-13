soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} numeros PARES, e a soma entre eles é {}.'.format(cont,soma)) 
    
    
