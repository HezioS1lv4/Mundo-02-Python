print('===Desafio 038===')

num1 = int(input('1o Numero? '))
num2 = int(input('2o Numero? '))

if num1 > num2:
    print('O primeiro Valor {} é MAIOR!'.format(num1))
elif num2 > num1:
    print('O segundo Valor {} é MAIOR!'.format(num2))
elif num1 == num2:
    print('Não existe valor maior, os dois {} e {} são IGUAIS!'.format(num1, num2))
