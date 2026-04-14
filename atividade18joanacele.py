numero = int(input('Digite um número: '))
par = numero % 2
if numero > 0 and par == 0 :
    print(f'{numero} é par postivo. ')
elif numero < 0 and par == 0 :
    print(f'{numero} é par negativo.')
elif  numero > 0 and par != 0 :
    print(f'{numero} é impar positivo. ')
elif numero < 0 and par != 0 :
    print(f'{numero} é impar negativo.')
elif numero == 0:
    print(f'{numero} é neutro.')