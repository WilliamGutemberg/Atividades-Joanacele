#Ler um valor e ver se é maior que 10 ou não.
numero = int(input('Digite um número: '))
if numero > 10: 
    print(f'{numero} é maior que 10!')
elif numero < 10:  
    print(f'{numero} é menor que 10!')
elif numero == 10:
    print(f'{numero} é igual a 10!')