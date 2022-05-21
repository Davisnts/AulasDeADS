"""
Faça um programa que peça um numero correspondente a um ano,
e o algoritmo retorne ao usuario se aquele é um ano bissexto, ou não
"""
ano = int(input('Qual ano voce deseja saber se é bisexto ou não ? '))
bano = ano%4
if bano == 0:
    print (f'o ano {ano} é bissexto')
else:
    print (f'o ano {ano} não é bissexto')
