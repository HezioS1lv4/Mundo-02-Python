print('===Desafio 042===')

n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM formar triângulo!', end='')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')



