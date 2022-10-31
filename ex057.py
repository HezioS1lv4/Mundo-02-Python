sexo = 'Mm, Ff'

while sexo == 'Mm' or 'Ff':
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper()[0].strip()
    if sexo == 'M':
        print('Seu sexo é Masculino!')
    if sexo == 'F':
        print('Seu sexo é Feminino!')

    if sexo != 'M' and sexo != 'F':
        print('Escolha uma opção válida!')

# EX do guanabara
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
