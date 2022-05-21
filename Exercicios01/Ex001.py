b = '='*35
print(f'{b}')
play = str(input('escolha par ou impar ? '))
play1 = int(input('Escolha um numero ? '))
play2= int(input('escolha um numero ? '))
logica = (play1+play2)%2
if logica == 0:
    log = 'Par'
else:
    log = 'Impar'
if logica == 0 and play == 'par':
    print(f'Voce Ganhou! pois {play1+play2} é {log}\n{b}')
elif logica == 1 and play == 'impar':
    print(f'Voce Ganhou! pois {play1+play2} é {log}\n{b}')
else:
    print(f'Voce Perdeu! pois {play1+play2} é {log}\n{b}')
