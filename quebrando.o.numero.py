#primeira forma

from math import trunc
num = float(input('Digite um numero:'))
raiz = trunc(num)
print('O valor digitado foi {} e sua porção inteira e {}.'.format(num,raiz))

#segunda forma

import math
num = float(input('Digite um numero:'))
raiz = math.trunc(num)
print('O valor digitado foi {} e sua porção inteira e {}.'.format(num,raiz))
