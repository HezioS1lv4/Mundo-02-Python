soma = 0  # Acumulador
cont = 0  # Contador
for n in range(1, 501, 2):   # if n % 2 == 1:
    if n % 3 == 0:
        cont = cont + 1  # cont += 1
        soma = soma + n  # soma += n
print('A soma de {}  valores solicitados é de {}'.format(cont, soma))

