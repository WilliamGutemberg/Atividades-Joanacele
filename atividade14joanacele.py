numero = input('Digite um número: ')
numero = int(numero)
multiplo = numero % 3
if multiplo == 0:
    print('Múltiplo de 3. ')
else:
    print('Não é multiplo de 3.')
