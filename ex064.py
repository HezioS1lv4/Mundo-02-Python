cont = soma = num = 0
num = int(input('Digite [999] para finalizar: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite [999] para finalizar: '))
print('Contagem de termos: {}'.format(cont))
print('Valor da soma {}'.format(soma))
print('FINALIZADO!')