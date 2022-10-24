print('===Desafio 040===')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print('Sua média foi {:.1f} e sua situação é:'.format(media))
if media >= 7.0:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')

# entre 5.0 e 6.9

# if media >= 5 and media < 7:
#    print('RECUPERAÇÃO')
