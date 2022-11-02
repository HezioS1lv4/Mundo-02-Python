# Método Guanabara
from random import randint
v = 0
while True:
    jogador = int(input('Diga um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print(f'Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {v} vezes.')

# Meu método (imcompleto)
'''import random
pc = random.randint(1, 10)

n = 0
while True:
    print('-='*20)
    print('Vamos brincar de PAR ou IMPÁR ^^')
'''#    print('''    [P] PAR
#    [I] IMPAR''')
'''    print('-='*20)
    opcao = str(input('[I] ou [P]? ').upper().strip())
    n = int(input('Diga um valor: '))
    soma = n + pc
    par = soma % 2 == 0
    impar = soma % 2 == 1

    if par:
        result = 'Deu PAR'
    if impar:
        result = 'Deu IMPAR'
    print('--'*20)
    print(f'Você jogou {n}, e o pc {pc}. Total de {soma}, {result}!!')
    print('--'*20)
    # FALTA RESOLVER A QUESTÃO DO VENCEU OU PERDEU, E O CONTADOR
    if opcao =='''
