#Calcule o salario de um vend  edor, sabendo que ele recebe o salario mais 15% de comissões
v1 = float(input('Quando você recebe de salario? '))
v2 = float(input('Quando você vendeu ? '))
v3 = v2*0.15
v4 = v3+v1
v5 = v4*0.74
p = '='*45
print(f'{p}\nVocê recebeu R${v1:.2f} do seu salario\nVocê vendeu R${v2:.2f} em produtos\nVocê recebeu R$ {v3:.2f} em comissoes\nSeu rendimento bruto é R$ {v4:.2f}\nPorem devido a alta carga tributaria do brasil você só recebe R$ {v5:.2f}\n{p}')
