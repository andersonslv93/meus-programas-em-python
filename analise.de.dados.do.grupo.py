dezoito = homem = mulher = 0
while True:
    #CADASTRO
    print('-' * 35)
    print('      CADASTRE UMA PESSOA')
    print('-' * 35)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    print('-' * 35)
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    
#SOMATORIO TOTAL

    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {dezoito}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
