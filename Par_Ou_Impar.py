from time import sleep
from random import randint
computador = randint(0,10)
jogador = input('Você quer ser Par ou Impar? ')
if jogador == 'par':
    print('OK,Você escolheu par!Então computador será impar.' )
elif jogador == 'impar':
    print('OK,Você escolheu impar!Então computador será par.')
num1 = int(input("escolha um numero jogador : "))
print("O computador escolheu: {}".format(computador))
conta = (num1 + computador) % 2
sleep(1)
print('--IMPAR--')
sleep(1)
print('--OU--')
sleep(1)
print('--PAR--')
if conta == 0:
    if jogador == 'par':
        print('você ganhou!')
    else:
        print("Você perdeu!")
if conta == 1:
    if jogador == 'impar':
        print('você ganhou!')
    else:
        print("Você perdeu!")


