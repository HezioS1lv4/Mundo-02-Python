# for c in range(0, 6, 2):
#    print(c)
# print('FIM')

# for c in range(6, 0, -1):
#     print(c)
# print('FIM')

# n = int(input('Digite um número: '))
# for c in range(0, n + 1):
#     print(c)
# print('FIM')

# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))

# for c in range(i, f + 1, p):
#     print(c)
# print('FIM')

S = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    S = S + n  # S += n
print('O somatório de todos os valores foi {}'.format(S))