temp = []
dados = []
cont = maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso ')))

    if len(dados) == 0:
        maior = temp[1]
        menor = temp[1]
    if temp[1] > maior:
        maior = temp[1]
    if temp[1] < menor:
        menor = temp[1]
    
    dados.append(temp[:])
    temp.clear()
            
    cont += 1
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    if c == 'N':
        break

print('-=' * 40)
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi {maior}KG de ',end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}... ', end='')
print(f'\nO menor peso foi {menor}KG de ',end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}... ',end='')
