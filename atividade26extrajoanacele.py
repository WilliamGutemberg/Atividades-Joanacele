numero = int(input('Digite um número: '))
if numero > 0 and numero <= 10:
    print('Pequeno.')
elif numero >= 10 and numero <= 100:
    print('Médio.')
elif numero > 100:
    print('Grande. ')
else:
    print('Negativo ou zero')