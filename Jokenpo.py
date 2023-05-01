from random import randint
itens = ("Pedra","Papel","Tesoura")
computador  = randint(0,2)
print("*OPCÕES*","\nPEDRA = [0]","\nPAPEL = [1]","\nTESOURA = [2]")
jogador = int(input('Faça sua escolha: '))
if jogador == 0:
      if computador == 0:
            print("Empate")
      elif computador == 1:
            print("Você perdeu!")
      elif computador == 2:
            print("Você Ganhou!")
      else:
            print("Inválido")
      print("Voce jogou Pedra e o computador {}".format(itens[computador]))

if jogador == 1:
      if computador == 0:
            print("Você Ganhou!")
      elif computador == 1:
            print("Empate")
      elif computador == 2:
            print("Você Perdeu!")
      else:
            print("Inválido")
      print("Você jogou Papel e o computador {}".format(itens[computador]))

if jogador == 2:
      if computador == 0:
            print("Você Perdeu!")
      elif computador == 1:
            print("Você Ganhou!")
      elif computador == 2:
            print("Empate")
      else:
            print("Inválido")
      print("Você jogou Tesoura e o computador {}".format(itens[computador]))
