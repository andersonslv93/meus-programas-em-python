from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano do nascimento? '))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR.')
elif idade > 19 and idade <= 25:
    print('Categoria SENIOR.')
else:
    print('Categoria MASTER.')
