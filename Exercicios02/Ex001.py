nota1=0
nota2=0
nota3=0

nome = str(input('Qual o nome do aluno ? '))
nota1 = float(input('Qual a 1ª nota do aluno ? '))
while nota1 <=0 or nota1 > 10 :
    nota1 = float(input('Nota invalida insira novamente !! '))
nota2 = float(input('Qual a 2ª nota do aluno ? '))
while nota2 <=0 or nota2> 10 :
    nota2 = float(input('Nota invalida insira novamente !! '))
nota3 = float(input('Qual a 3ª nota do aluno ? '))
while nota3 <=0 or nota3> 10 :
    nota3 = float(input('Nota invalida insira novamente !! '))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f'Parabens {nome} voce foi aprovado com a média de {media:.2f}')
elif media >=5 and media <= 6.9:
    print(f'Olá {nome} infelizmente você esta de recuperaçao pois sua media foi de {media:.2f}')
else:
    print(f'Caro {nome} voce reprovado pois sua media final foi de {media:.2f}')
