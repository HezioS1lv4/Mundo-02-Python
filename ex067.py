c = 0
while True:
    print('-'*20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:  # Para fazer nosso stop caso o numero seja negativo!
        break
    print('-'*20)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
