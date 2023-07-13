from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):    
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E tambem tivemos {} pessoas menores de idade.'.format(menor))
