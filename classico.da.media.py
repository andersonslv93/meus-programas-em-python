n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota '))
media = n1 + n2
media1 = media / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1,n2,media1))
if media1 < 5.0:
    print('REPROVADO')
elif media1 >= 5.0 and media1 <= 6.9:
    print('RECUPERAÇÃO')
elif media1 >= 7.0:
    print('APROVADO')
    
    
