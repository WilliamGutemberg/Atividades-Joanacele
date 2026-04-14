numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 == numero2:
    print(f'{numero1} é igual {numero2}')
else:
    print(f'{numero1} é diferente de {numero2}')
    diferenca = numero1 - numero2
    print('A diferença de ' f'{numero1} e 'f'{numero2} é 'f'{diferenca}.')