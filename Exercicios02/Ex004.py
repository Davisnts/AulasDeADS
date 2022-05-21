CidadeA = int(80000)
CidadeB = int(200000)
Anos = int(0)
while CidadeA <= CidadeB:
    CidadeA = CidadeA*1.04
    CidadeB = CidadeB*1.008
    Anos += 1
print(f'A populaçao da cidade A é de {CidadeA:.0f} enquando a da cidade B é de {CidadeB:.0f} \nOu seja a Cidade A ultrapassou a Cidade B em numero de habitantes no ano {2022+Anos}')

