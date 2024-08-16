num = int(input('escreva um numero de até 4 caracteres'))

print('unidade: {}'.format(num%10))
print('dezena: {}'.format(((num%1000)%100)//10))
print('centena: {}'.format((num%1000)//100))
print('milhar: {}'.format((num//1000)))

numstr = str(num)
print('unidade: {}'.format(numstr[3]))
print('dezena: {}'.format(numstr[2]))
print('centena: {}'.format(numstr[1]))
print('milhar: {}'.format(numstr[0]))
