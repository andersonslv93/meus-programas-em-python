#Quero saber se o primeiro nome e 'santo'

cidade = str(input('Qual é a cidade em que você nasceu? ')).strip()
print(cidade[:5].lower() == 'santo')
