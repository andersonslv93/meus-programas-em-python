from datetime import date
atual = date.today().year
ano = int(input('Qual o ano de nascimento? '))
idade = atual - ano
alistamento = idade - 18
data_alistamento = atual - alistamento

if idade > 18:
    print('Quem nasceu em {} tem {} em {}.'.format(ano,idade,atual))
    print('Você deveria ter se alistado em {} anos.'.format(alistamento))
    print('Seu alistamento foi em {}.'.format(data_alistamento))
elif idade <=18:
    print('Quem nasceu em {} tem {} em {}.'.format(ano,idade,atual))
    print('Você deve se alistar IMEDIATAMENTE.')
