dados = []
pares = []
impares = []
for c in range(0,7):
    dados.append(int(input(f'Digite o {c+1}º valor: ')))
    for d in dados:
        if d % 2 == 0:
            pares.append(dados[:])
        else:
            impares.append(dados[:])
    dados.clear()
    pares.sort()
    impares.sort()
print('-=' * 40)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
