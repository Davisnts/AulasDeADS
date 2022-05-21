#Faça um programa pra uma loja de tinta,O programa devera pedir a largura e a altura da parede e calcular.
#Seu tamanho em metris quadrados.Considera que um litro de tinta é capaz de pintar 3m².
#O usuario também devera determinar o valor da tinta escolhida.
#Ao Final do programa determina o custo total de compras em tintas.
n1 = float(input('Digite a Largura da Parede: '))
n2 = float(input('Digite a Altura da Parede : '))
dinero = float(input('Digite o Preço da lata de tinta: '))
comp = n1*n2
qnt = comp/3
gasto = qnt*dinero
mold = '='*35
print(f'{mold}\no Comprimento da parede é {comp:.2f} m² \nSerão gastos {qnt:.2f} litros de tinta \nCustara R$ {gasto:.2f}\n{mold}')
