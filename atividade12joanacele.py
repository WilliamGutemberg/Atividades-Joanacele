numero1 = int(input('Digite um número:' ))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
print(f'{numero1}' '+' f'{numero2}''='f'{soma}')
if numero1 > numero2:
    print(f'{numero1} é maior.')
elif numero2  > numero1:
    print(f'{numero2} é maior. ')
else:
    print(f'{numero1}'' e 'f'{numero2}'' são iguais.' )