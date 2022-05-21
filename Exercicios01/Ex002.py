from random import randint
rand = randint(0, 59)
jogo = str(input('Escolha par ou Impar: '))
logica = rand%2
if logica == 0:
    log = 'Par'
else:
    log = 'Impar'
if logica == 0 and jogo == 'par':
    print(f'Voce Ganhou! pois {rand} é {log}')
elif logica == 1 and jogo == 'impar':
    print(f'Voce Ganhou! pois {rand} é {log}')
else:
    print(f'Voce Perdeu! pois {rand} é {log}')
