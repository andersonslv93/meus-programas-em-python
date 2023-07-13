#primeira forma

from math import sqrt
num1 = float(input('Qual o valor do cateto oposto?'))
num2 = float(input('Qual o valor do cateto adjacente?'))
soma = num1 ** 2 + num2 ** 2
total = sqrt(soma) 
print('O valor do comprimento da hipotenusa e de {:.2f}.'.format(total))

#segunda forma

import math
num1 = float(input('Qual o valor do cateto oposto?'))
num2 = float(input('Qual o valor do cateto adjacente?'))
hi = math.hypot(num1, num2)
print('O valor do comprimento da hipotenusa e de {:.2f}.'.format(hi))
