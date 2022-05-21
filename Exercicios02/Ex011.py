from math import inf
b = '='*40
clientes = 0
gordo = -inf
magro = inf
alto = -inf
baixo = inf
Codgordo = 0
Codmagro = 0
Codalto = 0
Codbaixo = 0
somaP = 0
somaA = 0
while True:
    codigo = input("Digite o codigo do cliente \n(utilize 0 para parar de adicionar clientes!) : ")
    if codigo == "0":
        break
    clientes+=1
    altura = int(input('Qual a altura do cliente ? (Utilize centimetros) Ex : 170 para 1.70 '))
    peso = float(input('Qual o peso do cleinte ? (Utilize Quilos) Ex 64.0 para 64 quilos '))
    somaA+=altura
    somaP+=peso
    if altura > alto:
        alto = altura
        Codalto = codigo
    if altura < baixo:
        baixo = altura
        Codbaixo = codigo
    if peso > gordo:
        gordo = peso
        Codgordo = codigo
    if peso < magro:
       magro = peso
       Codmagro = codigo
    MedAltura = somaA/clientes
    MedPeso = somaP/clientes
print(f'{b}\n'
      f'A academia tem {clientes} clientes'
      f'O Codigo do clientes mais Alto é {Codalto} e sua altura é {alto}\n'
      f'O Codigo do clientes mais baixo é {Codbaixo} e sua altura é {baixo}\n'
      f'O Codigo do clientes mais gordo é {Codgordo} e seu peso é {gordo}\n'
      f'O Codigo do clientes mais magro é {Codmagro} e sua altura é {magro}\n'
      f'A media de Alturas dos clientes é de {MedAltura:.2f} e a Media de Peso é {MedPeso:.2f}\n{b}')