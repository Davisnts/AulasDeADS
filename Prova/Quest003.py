"""
Faça um programa que faça 5 perguntas ao usuario, em que ele respondera [1] para sim e [0] para não
As perguntas são :
1: Você esteve na noite anterior ?
2: Você esteve no local do crime ?
3: Existe alguma divergencia entre você e a vitma?
4: Tem algum debito entre você e a vitma?
5: Mora perto da Vitma?
"""

print('Reponda as perguntas utilizando [0] para não e [1] para sim ')
noite = int(input('Voce esteve presente na noite anterior ? '))
local = int(input('Você Esteve no local do crime ? '))
divergencia = int(input('Existe uma divergencia entre você e a vitma ? '))
debito = int(input('Tem algum debito com a vitma ? '))
mora = int(input('Você mora perto da vitma ? '))
somaf = noite+local+divergencia+debito+mora
if somaf == 5:
    (print('Você é o Assassino'))
elif somaf == 3 or somaf == 4:
    (print('Você é Suspeito de cometer o Assasinato'))
elif somaf == 1 or somaf == 2:
     (print('Você é Cumplice'))
elif somaf == 0:
     (print('Você é Inocente '))
else:
    print('Refaça o teste por favor')
