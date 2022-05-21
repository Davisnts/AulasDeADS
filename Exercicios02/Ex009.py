num = int(input('Qual numero voce deseja saber se ele é primo ? '))
primo = 0

for numprimo in range (1, (num + 1)):
    if num % numprimo ==0:
        numprimo += 1
if numprimo == 2:
    print (f'o numero {num} é primo !')
else:
    print (f'o numero {num} não é primo !')


