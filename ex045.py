print('===Desafio 045===')

# import random
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')


print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogada]))
print('-=' * 11)

if computador == 0:  # PEDRA
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE!')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:  # PAPEL
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:  # TESOURA
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
