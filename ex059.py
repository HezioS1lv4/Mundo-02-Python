num = 0

# IMCOMPLETO

while num != 5:
    print('---Calculadora H.S---')
    num1 = int(input('Digite o 1° numero: '))
    num2 = int(input('Digite o 2° numero: '))
    print('''   
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    num = int(input('Sua opção: '))

    if num == 1:
        soma = num1 + num2
        print('A valor da soma é {}'.format(soma))
    if num == 2:
        multiplicar = num1 * num2
        print('O valor da multiplicação entre {}X{} é {}'.format(num1, num2, multiplicar))
    if num == 3:
        maior = num1
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print('O maior valor é {}'.format(maior))
    if num == 4:
        print('Informe os numeros novamente:')
        num1 = int(input('Digite o 1° numero: '))
        num2 = int(input('Digite o 2° numero: '))
    if num == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print('=-=' * 10)
#    sleep(2)
print('Finalizado com sucesso!')
