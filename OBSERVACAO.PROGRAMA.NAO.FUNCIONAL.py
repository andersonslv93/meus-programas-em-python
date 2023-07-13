#primeira forma de usar a biblioteca

from math import sqrt 
num = int(input('Digite um numero:'))
raiz = sqrt(num)
print('A raiz de {} é de {:.2f}.'.format(num,raiz))

-------
#segunda forma de usar a biblioteca 

import math 
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é de {:.2f}.'.format(num,raiz))

------------
#arredondando a raiz para cima CEIL ou para baixo FLOOR

from math import sqrt
num = int(input('Digite um numeroo:'))
raiz = math.sqrt(num)
print('A raiz de } é de {}.'.format(num, math.ceil(raiz)))
