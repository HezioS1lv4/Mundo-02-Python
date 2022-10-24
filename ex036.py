print('===Desafio 036===')

print('Empréstimo bancário!')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você recebe? R$'))
anos = int(input('Em quantos anos você irá pagar? R$'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')











