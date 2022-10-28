sexo = 'Mm, Ff'

while sexo == 'Mm' or 'Ff':
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper()
    if sexo == 'M':
        print('Seu sexo é Masculino!')
    if sexo == 'F':
        print('Seu sexo é Feminino!')

    if sexo != 'M' and sexo != 'F':
        print('Escolha uma opção válida!')
