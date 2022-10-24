print('===Desafio 041===')
from datetime import date

nascimento = int(input('Qual o seu ano de nascimento: '))
idade = date.today().year - nascimento

print('Sua idade é de {}'.format(idade))

if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
