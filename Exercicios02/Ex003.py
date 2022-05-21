"""from datetime import date
anoAtual = date.today().year"""
nome = str(input('Qual seu nome ? '))
dia = int(input('Qual dia voce nasceu ? '))
mes = int(input('Qual mes que voce nasceu ? '))
ano = int(input('Qual ano voce nasceu ? '))
sexo = str(input('Qual seu sexo ? (Utilize F/M)')).upper()
#while sexo != 'M' and sexo != 'F':
while sexo not in 'MFmf':
    sexo = str(input('Opçao invalida !! \n Tente novamente '))
ctps = int(input('Qual seu numero de CTPS ? (digite 0 caso não possua)'))
"""ctb = str(input('Você possui carteira de trabalho (Utilize S/N)')).upper()
while ctb not in 'snSN':
    ctb = str(input('Opçao invalida !! \n Tente novamente '))"""
if ctps != '0':
    salario = str(input('Qual seu salario? '))
    anor = int(input('Qual seu ano de registo ? '))
    if sexo == 'M':
        print(f'Sr {nome} voce nasceu no dia {dia} do mes {mes} no ano de {ano} voce tem {anoAtual-ano} Anos\nVocê recebe um salario de {salario} e voce ira se aposentar no ano de {anor+35}')
    if sexo == 'F':
        print(f'Sra {nome} voce nasceu no dia {dia} do mes {mes} no ano de {ano}voce tem {anoAtual-ano} Anos\nVocê recebe um salario de {salario} e voce ira se aposentar no ano de {anor+30}')
else:
    if sexo == 'M':
        print(f'Sr {nome} voce nasceu no dia {dia} do mes {mes} no ano de {ano} voce tem {anoAtual-ano} e como voce nao tem carteira de trabalho nao é prossivel determinar quando você ira se aposentar')
    if sexo == 'F':
        print(f'Sra {nome} voce nasceu no dia {dia} do mes {mes} no ano de {ano}voce tem {anoAtual-ano} e como voce nao tem carteira de trabalho nao é prossivel determinar quando você ira se aposentar')


