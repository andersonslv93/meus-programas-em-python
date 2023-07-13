import random
from time import sleep 
#jogada minha

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

#jogada computador

computador = random.randint(0,2)
      
print('-=-' * 20)
      
if jogador == computador:
    print('EMPATOU')
elif jogador == 0 and computador == 1:
    print('Computador jogou PAPEL')
    print('Jogador jogou PEDRA')
    print('COMPUTADOR VENCE')
elif jogador == 0 and computador == 2:
    print('Computador jogou TESOURA')
    print('Jogador jogou PEDRA')
    print('JOGADOR VENCE')
elif jogador == 1 and computador == 0:
    print('Computador jogou PEDRA')
    print('Jogador jogou PAPEL')
    print('JOGADOR VENCE')
elif jogador == 1 and computador == 2:
    print('Computador jogou TESOURA')
    print('Jogador jogou PAPEL')
    print('COMPUTADOR VENCE')
elif jogador == 2 and computador == 0:
    print('Computador jogou PEDRA')
    print('Jogador jogou TESOURA')
    print('COMPUTADOR VENCE')
elif jogador == 2 and computador == 1:
    print('Computador jogou PAPEL')
    print('Jogador jogou TESOURA')
    print('JOGADOR VENCE')
else:
    print('JOGADA INVALIDA')
print('-=-' * 20)
