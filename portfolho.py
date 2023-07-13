from time import sleep
primeiro = int(input('Primeiro Valor: '))
segundo = int(input('Segundo valor: '))
opção = 0

while opção != 5:

    opção = int(input('''=-==-==-==-==-==-==-==-=
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
>>>>> Qual é a sua opção? '''))

    if opção == 1:
        print('A soma entre {} + {} é {}.'.format(primeiro,segundo, primeiro + segundo))
    if opção == 2:
         print('A multiplicação entre {} * {} é {}.'.format(primeiro, segundo, primeiro * segundo))
    if opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            if segundo > primeiro:
                maior = segundo
        print('Entre {} e {}, o maior é {}.'.format(primeiro,segundo, maior))
    if opção == 4:
        primeiro = int(input('Primeiro Valor: '))
        segundo = int(input('Segundo valor: '))
    if opção == 5:
        print('Finalizando...')
        sleep(5)
    else:
        print('Opção inválida. Tente novamente!')
        sleep(2)
print('''=-==-==-==-==-==-==-==-=
Fim do programa! Volte sempre!''')
