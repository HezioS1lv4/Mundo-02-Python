
soma = 0
for n in range(1, 7):
    num = int(input('Digite o {}° numero inteiro: '.format(n)))

    if num % 2 == 0: 
        soma += num  # OU soma = soma + num    # num se par, vira soma que tem valor de 0
print('A soma dos valores PARES é: {} '.format(soma))
