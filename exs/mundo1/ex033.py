n1 = float(input('escollha o primeiro numero '))
n2 = float(input('escollha o segundo numero '))
n3 = float(input('escollha o terceiro numero '))

 
if n1>n2 and n1>n3:
    maior = n1
else: 
    if n2 > n3:
        maior = n2
    else:
        maior = n3

if n1<n2 and n1<n3:
    menor = n1
else: 
    if n2 < n3:
        menor = n2
    else:
        menor = n3

print('o maior numero digitado foi {} e o menor numero digitado foi {}'.format(maior, menor))