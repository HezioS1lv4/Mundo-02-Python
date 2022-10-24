print('===Desafio 039===')
import datetime
# from datetime import date

ano = int(input('Qual o seu ano de nascimento: '))
idade = datetime.date.today().year - ano
prazo = 18

print('Sua idade é {} Anos!.'.format(idade))

if idade == 18:
    print('Está na hora de você se alistar!')
elif idade < 18:
    print('Você ainda vai se alistar no Serviço Militar.')
    print('Falta {} ano(s) para o prazo!'.format(prazo - idade))
elif idade > 18:
    print('Você já passou o prazo para o alistamento.')
    print('Passou {} ano(s) do prazo!'.format(idade - prazo))
