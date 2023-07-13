from random import randint
from time import sleep
cont = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)

#COMPUTADOR E JOGADOR
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor: '))
    total = computador + jogador
    pi = str(input('Par ou Impar? [P/I] ')).upper().strip()
    
#RANDOMIZAR, PAR OU IMPAR
    if total % 2 == 0 and pi == 'P':
        cont += 1
        print('-' * 60)
        print('Você jogou {} e o computador {}. Total de {}, DEU PAR, VOCÊ VENCEU!'.format(jogador,computador, total))
        print('-' * 60)
        print('Vamos jogar novamente...')
        sleep(3)
    if total % 2 != 0 and pi == 'I':
        cont += 1
        print('-' * 30)
        print('Você jogou {} e o computador {}. Total de {}, DEU IMPAR, VOCÊ VENCEU!'.format(jogador,computador, total))
        print('-' * 60)
        print('Vamos jogar novamente...')
        sleep(3)
    if total % 2 == 0 and pi == 'I':
        print('-' * 30)
        print('Você jogou {} e o computador {}. Total de {}, DEU PAR, VOCÊ PERDEU!'.format(jogador, computador, total))
        print('-' * 60)
    if total % 2 != 0 and pi == 'P':
        print('-' * 60)
        print('Você jogou {} e o computador {}. Total de {}, DEU IMPAR, VOCÊ PERDEU!'.format(jogador,computador, total))
        print('-' * 60)
    if total % 2 == 0 and pi == 'I' or total % 2 != 0 and pi == 'P':
        break 
print('GAME OVER! Você venceu {} vezes.'.format(cont))
