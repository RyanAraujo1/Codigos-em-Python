from random import randint
from time import sleep
computador = randint(0,5)
print('-'*60)
print("Vou  pensar em um número de 0 a 5. Tente adivinha....")
print('-'*60)
jogador = int(input("Em que número eu pensei:"))
print('Processando...')
time.sleep(2)
if jogador == computador:
    print('PARABÉNS!Você ganhou.')
else:
    print('Você errou!Eu pensei no número {} e não no número {}'.format(computador,jogador))
