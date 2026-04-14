numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 >= 0 and numero2 >= 0:
    soma = numero1 + numero2
    print(f'{numero1}' '+' f'{numero2}')
    print(f'{soma}')
elif numero1 < 0 or numero2 < 0:
    produto = numero1 * numero2
    print(f'{numero1}' '*' f'{numero2}')
    print(f'{produto}')