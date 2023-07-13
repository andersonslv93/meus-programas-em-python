from random import randint
from time import sleep
computador = randint(0,5) #faz o computador 'PENSAR'
print('-º-' * 20)
print('\033[4:31:40mAdivinhe o numero que estou pensando.')
print('.º.' * 20)

jogador = int(input('O numero que você está pensando é...')) #pensamento do jogador
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('Eu pensei no número {}, e você no número {}. Parabéns, você venceu!!'.format(computador,jogador))
else:
    print('Eu pensei no número {}, e você no número {}. Eu venci! Boa sorte na proxima!'.format(computador,jogador))
    