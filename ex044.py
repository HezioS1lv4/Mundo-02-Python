print('===Desafio 044===')

# print('='*9 + 'Mercado H.S' + '='*9)
print('{:=^25}'.format('Mercado H.S'))
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = valor - (valor * 10/100)
elif opcao == 2:
    total = valor - (valor * 5/100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('Opção Inválida de pagamento')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,total))




