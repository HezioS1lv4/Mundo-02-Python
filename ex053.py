# Detector de Palíndromo
# frases que mesmo sendo ao contrário mantém o sentido

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''   # OU inverso = junto[::-1]  Sem precisar da estrutura de for
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')
print(junto, inverso)
