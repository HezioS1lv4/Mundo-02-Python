print('--'*10)
print('{:^20}'.format('Loja H.S'))
print('--'*10)
total = maiorq = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        maiorq += 1

    if cont == 1:  # OU -> or preco < menor:
        menor = preco
        barato = produto
    else:  # Anotação anterior serve com a mesma funcionalidade esse else, tornando o código simplificado
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print()
print(f'O total gasto foi de R${total:.2f}')
print(f'O total de produtos maiores que R$1000 é de {maiorq}')
print('O menor produto ({}) e custou R$ {:.2f}'.format(barato ,menor))
print('{:-^40}'.format('FIM DO PROGRAMA'))
