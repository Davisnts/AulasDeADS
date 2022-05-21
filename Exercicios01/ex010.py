lado1 = int(input('Qual o comprimento do primeiro lado do triangulo ? '))
lado2 = int(input('Qual o comprimento do Segundo lado do triangulo ? '))
lado3 = int(input('Qual o comprimento do Terceiro lado do triangulo ? '))
if lado > 0 and  lado2 > 0 and lado3 > 0:
    if lado1 == lado2 == lado3:
        print(f'Triângulo Equilátero')
    elif lado1 != lado2 != lado3:
        print(f'Triângulo Escaleno')
    else:
        print(f'Triângulo Isósceles')
