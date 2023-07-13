from random import randint
computador = randint(0,10)
cont = 0

jogador = int(input('''Sou seu computador...
Acabei de pensar em número entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual é o seu palpite? '''))

while jogador > computador:
    cont += 1
    jogador = int(input('Menos... Tente mais uma vez: '))
while jogador < computador:
    cont += 1
    jogador = int(input('Mais... Tente mais uma vez: '))
print('Acertou com {} tentativas. Parabéns!'.format(cont))
