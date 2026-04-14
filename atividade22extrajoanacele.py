try:
    valor = int(input('Digite um valor: '))
    if valor >= 10 :
        print('Alto')
    else:
        print('Baixo')
except:
    print('Entrada inválida.')
