'''
num = list()
while num != -999:
    num = float(input('Digite a nota: '))
    if num >= 1 and num <= 10:
#        print('Está entre 1 e 10')
        print('Para sair [-999]')
#        print(num)
        'Os calculos entrariam dentro desse if, e dps so pede pra printar no final fora da identação!'
        media = (num + num) / 2
        print('A média das notas é {}'.format(num))
    elif num == -999:
        print('Programa finalizado com sucesso!')
    else:
        num = 0
        print('Escreva uma opção correta! Entre 1 e 10')
'''

'''
notas = list()

while 1:

    nota = float(input('Inserir nota: '))
    if nota == -999:
        print('\nNotas Inseridas:', notas, '\n')
        break
    elif nota < 0 or nota > 10:
        print('digite nota entre 0 e 10')
        nota = 0
    elif nota > 0 or nota < 10:
        notas.append(nota)
    print(nota)
print('lista de notas:', notas, '\n')

def mediaiesb(dados):
    n = len(dados)
    s = 0
    for x in dados:
        s = s + x
    return s/n
'''

'Exercícios do ricardo ^'

from math import factorial

n = int(input('Digite um numero: '))
f = factorial(n)
print('O factorial de {} é {}'.format(n, f))