lista = []
maior = menor = 0
for c in range(0,5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    
    lista.append(n)
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n       
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for l, v in enumerate(lista):
    if v == maior:
        print(f'{l}...',end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for l, v in enumerate(lista):
    if v == menor:
        print(f'{l}...',end=' ')
