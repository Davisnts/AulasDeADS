from math import inf
"""maior = -321
menor = 321"""
b = '='*35
maior = -inf
menor = inf
ctemp = 0
somat = 0
tem = 'S'
while tem == 'S':
    temp = float(input('Qual foi a temperatura registrada ? '))
    if temp > maior:
         maior=temp
    if temp < menor:
        menor = temp
    tem = str(input('Deseja mais incluir uma temperatura ? (utilize S para sim)')).upper()
    somat += temp
    ctemp +=1
print (f'{b}\nForam Registradas {ctemp} temperaturas\nA maior temperatura registrada foi {maior}ºC\nA menor temperatura registrada foi {menor} ºC\nA média Final das temperaturas foi de : {somat/ctemp:.2f} ºC\n{b}')
