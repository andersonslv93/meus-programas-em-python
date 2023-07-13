import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
sorteio = [aluno1, aluno2, aluno3]
escolhido = random.choice(sorteio)
print('O aluno sorteado foi {}.'.format(escolhido))
