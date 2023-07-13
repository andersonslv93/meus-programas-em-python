n = int(input('Digite um número: '))
c = str(input('Quer continuar? [S/N] ')).upper().strip()
cont = 0
soma = 0
maior = 0
menor = 0
media = 0
while c == 'S':
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    if c == 'N':
        soma += n
        cont += 1
        media = soma / cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
