numero = int(input('Digite um número: '))
par = numero % 2 
if par == 0 and numero >=0:
    print(f'{numero} é par positivo. ')
elif par == 0 and numero < 0:
    print(f'{numero} é par negativo.')
else:
    print(f'{numero} é impar.')