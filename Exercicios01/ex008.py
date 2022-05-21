nome = str(input('Qual seu nome ? '))
altura = float(input('Qual sua altura ? '))
peso = float(input('Qual seu peso ? '))
imc = peso/altura**2
if imc <= 18.5:
   print(f'Caro(a) {nome} Você esta com baixo peso')
elif imc >= 18.5 and imc < 24.9:
   print(f'Caro(a) {nome} Você esta com peso normal ')
elif imc >= 25.0 and imc < 29.9:
   print(f'Caro (a) {nome } Voce esta com sobre peso')
elif imc >= 30.0 and imc < 34.9:
   print(f'Caro (a) {nome } Voce esta com obesidade')
elif imc >=35.0 and imc < 39.9:
   print(f'Caro (a) {nome } Voce esta com obesidade severa')
elif imc >=40:
   print(f'Caro (a) {nome } Voce esta com obesidade mórbida')
