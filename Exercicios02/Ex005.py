NCidadeA = str(input('Qual o nome da cidade A ? '))
CidadeA = int(input(f'A {NCidadeA} tem quantos Habitantes '))
NCidadeB = str(input('Qual o nome da cidade B ? '))
CidadeB = int(input(f'A {NCidadeB} tem quantos Habitantes ')
CCidadeA = float(input(f'Qual a Taxa de crescimento de {NCidadeA} ? '))
CCidadeB = float(input(f'Qual a Taxa de crescimento de {NCidadeB} ? '))
Anos = 0
while CidadeA <= CidadeB:
    CidadeA += CidadeA*CCidadeA
    CidadeB += CidadeB*CCidadeB
    Anos += 1
print(f'A populaçao de {NCidadeA} é de {CidadeA:.0f} enquando a de {NCidadeB} B é de {CidadeB:.0f} \n Ou seja {NCidadeA} ultrapassou {NCidadeB} em numero de habitantes no ano de {2022+Anos}')

