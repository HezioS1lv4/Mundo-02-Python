# Números Primos!
num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end=' ')
print('\033[mO número {} foi divisível {} vezes.'.format(num, tot))

if tot == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele NÃO é PRIMO')
