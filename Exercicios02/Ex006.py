n = int(input('Qual Numero voce precisa saber a tabuada ? '))
while n == 0:
  print ('Numero invalido tente novamente')
  n = int(input('Qual Numero voce precisa saber a tabuada ? '))
b = '='*35
print (f'{b}\nA tabuada de {n} é\n')
for tab in range (1,11):
  print (f'{n} X {tab} = {n*tab}')
print(f'{b}')

