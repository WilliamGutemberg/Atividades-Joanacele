numero = int(input('Digite um numero inteiro: '))
if numero > 0:
    raiz_aproximada = numero **0.5
    print('A raiz aproximada de ' f'{numero}' ' é 'f'{raiz_aproximada} ')
else:
    print('Número invalido.')