tcarro = str(input('Qual tipo do carro que voce alugou ? (Executivo,Luxo,Especial ou Passeio)'))
dias = int(input('Quantos dias voce ficou com o carro ? '))
kmcar = int(input('Quantos Km voce rodou ?'))
if tcarro == 'Executivo':
    diaria = 380
    pkm = 1.30
elif tcarro == 'Luxo':
    diaria = 315
    pkm = 1.15
elif tcarro == 'Especial':
    diaria = 280
    pkm = 1.00
elif tcarro == 'Passeio':
    diaria = 250
    pkm = 0.85
km = kmcar*pkm
diasap = diaria*dias
print(f'Voce pagara R$ {km+diasap} de alguel R$ {diasap} de diarias e R$ {km} de kilometragem')
