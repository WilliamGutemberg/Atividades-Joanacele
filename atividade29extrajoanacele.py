numero = int(input('Digite um número: '))
multiplo_de_5 = numero % 5
if multiplo_de_5 == 0 and numero >= 50:
    print('Multiplo alto.')
elif multiplo_de_5 == 0 and numero <50 :
    print('Multiplo baixo.')
elif multiplo_de_5 != 0:
    print('Não é multiplo. ')