nome = str(input('Digite seu nome completo: ')).strip()

#processamento

separador = nome.split()

print('Muito prazer!')
print('Seu primeiro nome é {}.'.format(separador[0]))
print('Seu ultimo nome é {}.'.format(separador[len(separador)-1]))
