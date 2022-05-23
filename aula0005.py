'''Faça um programa que leia o nome do vendendor,e atribua  seu salario com base na tabela
---> ate 1  ano =  R$ 1280,00
---> de 1 ate 3 anos  = R$ 1690,00
---> 3 ate 5 anos = R$ 2100,00
Calcule tambem a comissao sobre as vendas, respeitando a tabela
---> vendas inferior ou igual a 20.000,00 comissoes de 5%
---> vendas acima de 20.000,00 e menos que 30.000,00 comissão de 8%
---> vendas acima de 30.000,00 - comissoes de 12%
Ao Final salario total do vendendor'''

func = str(input('Qual o seu nome ? '))
anos = int(input(f'Caro {func} Quanto tempo você trabalha nessa empresa? '))
vendas = float(input(f'Caro {func} Quanto você vendeu no ultimo mes? '))
if anos <=1:
    salario = 1280.00
elif anos > 1 and anos < 3:
    salario = 1690.00
elif anos > 3 and anos < 5:
    salario = 2100
else:
    salario = 2800
if vendas <= 20000:
    com = vendas*0.05
elif vendas > 20000 and vendas < 30000:
    com = vendas*0.08
else:
    com = vendas*0.12
b = '='*60
print(f'{b}\nOla {func} voce vendeu {vendas:.2f} e recebeu {com:.2f} de comissão\nJa que voce esta conosco a {anos} voce recebe um salario de {salario}\nA Sua remuneraçao total é de {salario+com}\n{b}')
