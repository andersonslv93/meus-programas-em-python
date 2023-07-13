numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if n >= 0 or n <= 20:
        break
print(f'Você digitou o número {numeros[n]}')
