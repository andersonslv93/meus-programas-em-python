print('Gerador de PA')
print('-=' * 12)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1
    termo += razao 
print('FIM')
