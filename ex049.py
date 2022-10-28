valor = int(input('Valor para medir tabuada: '))
num = 0

for n in range(1, 11):
    num = int(num + 1)
    resultado = (int(num * valor))
    print('{} X {} = {}'.format(num, valor, resultado))

# OU

nmr = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(nmr, c, nmr*c))
