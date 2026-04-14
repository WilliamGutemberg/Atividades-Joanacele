numero = int(input('Digite um número: '))
if numero >= 0 and numero <= 100:
    if numero % 2 == 0:
        print(f'{numero} é par no intervalo.')
    else:
        print(f'{numero} é impar no intervalo.')
else:
    print(f'{numero}''fora do intervalo.')
