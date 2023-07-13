nome = str(input('Digite seu nome completo:' )).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
totalletra = len(nome)
primeiro = nome.split()[0]
quantidadeletra = len(primeiro[0:])
print('Seu nome em maiúsculo é {}\nSeu nome em minúsculo é {}.\nSeu nome tem ao todo {} letras.\nSeu primeiro nome é {}, e ele tem {} letras.'.format(maiusculo, minusculo, totalletra, primeiro, quantidadeletra))
