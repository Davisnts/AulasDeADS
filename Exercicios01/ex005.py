fpag = str(input('Aceitamos Pix,Débito,Credito e Parcelamento\nQual sera a forma de pagamento ? '))
vproduto = float(input('Qual valor do produto ? '))
if fpag == 'Credito':
    parcelas = int(input('insira a quantidade de parcelas : '))
if fpag == 'Pix':
    cet = vproduto*0.90
elif fpag == 'Débito':
    cet = vproduto*0.95
elif fpag == 'Credito':
    vtotal = vproduto*1.10
    cet = (f'R$ {vtotal} parcelado em {parcelas} vezes de R$ {vtotal/vproduto}')
print(f'O valor a pagar será de R$ {cet}')
