numero = int(input('Digite um número: '))
if numero >= 0: 
    m2 = numero % 2 
    m3 = numero % 3 
    if m2 == 0 and m3 == 0:
        print(f'{numero} multiplo de 2 e 3.')
    else:
        print(f'{numero} não atende.')
if numero < 0:
    print(f'{numero} número inválido. ')