#Faça um programa que pergunte quando você ganha por dia,pergunte o numero de dia trabalhados
#Calcule e mostre o total do salario bruto.
#Monstre no Final
#Salario Bruto
#INSS - 11%
#IRPF - 7%
#FGTS - 8%
#Salario Liquido
mold='='*35
SalarioD = float(input('Quanto você recebe por dia ?: R$ '))
dias = int(input('Quantos dias voce trabalhou? '))
salariob =SalarioD*dias
inss = salariob*0.11
irrf = salariob*0.07
fgts = salariob*0.08
salariol = salariob*0.74
print(f'{mold}\nSeu Salario bruto é R$ {salariob}\né descotando R$ {inss:.2f} de INSS\né descontado R$ {irrf:.2f} de IRPF\né descontado R$ {fgts:.2f} de FGTS\nSeu salario liquido é R$ {salariol:.2f}\n{mold} ')
