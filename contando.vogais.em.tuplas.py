palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR',
            'PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end= ' ')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
