# BREAK
# Interrompe um while e joga pra fora da estrutura de repetição

'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')
'''
# While True = Loop infinito

'''n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))

# Como utilizar o f strings!! vv
print(f'A soma vale {s}')

nome = 'Hézio'
idade = 19
print(f'O {nome} tem {idade} anos!')'''
#////////////////////////////////////////////#

nome = 'Hézio'
idade = 19
salario = 833.2
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}!')
#          complemento, alinhado, 20vezes
