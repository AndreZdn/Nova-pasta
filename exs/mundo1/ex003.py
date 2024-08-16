n1 = int(input('escolha um numero: '))
n2 = int(input('escolha outro numero: '))
s = n1 + n2
# print('a soma entre', n1,'e', n2, 'é igual a', s)
print('a soma entre \033[1;35;42m{0}\033[m e \033[1;35;42m{1}\033[m  é igual a \033[1;35;42m{2}\033[m '.format(n1, n2, s))
print(n1.is_integer())
