num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para a conversção:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opçao = int(input('Sua opção: '))

if opçao == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL e {}.'.format(num, bin(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num,hex(num)[2:]))
else:
    print('Opção invalida! Digite uma das opçoes acima!')
