num = int(input('Qual numero voce deseja saber a fatorial ? '))
fac = num
while fac > 1:
    fac -= 1
    num *= fac
print (num)
