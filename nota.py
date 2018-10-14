#!/usr/bin/python3

# Media Anual
nota_primeiro_semestre = float (input('Favor informar sua nota do primeiro semestre: '))
nota_segundo_semestre = float (input('Favor informar sua nota do segundo semestre: '))

media = (nota_primeiro_semestre + nota_segundo_semestre) / 2

if media >= 7:
    print('Aprovado media: {}'.format(media))
elif media > 3:
    print('Recuperacao media: {}'.format(media))
else:
    print('Reprovado media: {}'.format(media))

