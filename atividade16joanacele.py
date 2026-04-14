numero = input('Valor: ')
print(type(numero))
if numero.isnumeric(): 
    numero = int(numero)
    quadrado = numero ** 2
    print(f'{quadrado}')
elif numero != int:
    print(f'{numero} não é númerico.')    