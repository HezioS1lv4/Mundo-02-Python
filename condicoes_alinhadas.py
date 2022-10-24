# Estruturas de Controles

nome = str(input('Qual o seu nome? '))


if nome == 'Hézio':
    print('Que nome diferente!')
elif nome == 'Hézio Silva dos Santos' or nome == 'Hézio Silva' or nome == 'Hézio Santos':
    print('Que nome lindo você tem!')
elif nome == 'Yan Lincon':
    print('Que nome raro!')
elif nome in 'Silva Santos Ferreira Gonçalves':
    print('O seu nome é bem popular!')
else:
    print('Seu nome é comum')
print('Tenha um bom dia {}!'.format(nome))

# elif só existe se tiver if
# else é uma estrutura opcional
