usr = str(input('Qual seu usuario ? '))
senha = str(input('Qual sua senha ? '))

while usr == senha or senha == '12345678':
    print ('Senha Invalida')
    senha = str(input('Qual a sua senha ?'))
