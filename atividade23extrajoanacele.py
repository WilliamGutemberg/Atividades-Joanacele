numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))
a = numero1 % 3
b = numero2 % 3
c = numero3 % 3
if a >= b >= c:
    print(a,b,c)
elif a >= c >= b:
    print(a,c,b)
elif b >= a >= c:
    print(b,a,c)
elif b >= c >= a:
    print(b,c,a)
elif c >= a >= b:
    print(c,a,b)
else:
    print(c,b,a)