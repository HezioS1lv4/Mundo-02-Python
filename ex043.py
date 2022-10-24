print('===Desafio 043===')
print('Calculadora de IMC')

peso = float(input('Qual é o seu peso (kg): '))
altura = float(input('Qual é a sua altura (m): '))

imc = peso / (altura ** 2)

print('O seu IMC é de {:.1f} e você está com: '.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
    