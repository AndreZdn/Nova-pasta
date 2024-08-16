
numes = int(input('Qual valor voce deseja converter? '))
print('=-='*10)
print('escolha para qual base voce deseja converter')
print('Binario[1]')
print('octal[2]')
print('Hecadeciaml[3]')
print('=-='*10)
res = int(input('digite o numero que representa a base'))

if res == 1:
    conversao = bin(numes)
    base = 'binario'
elif res == 2:
    conversao = oct(numes)
    base = 'octal'
elif res == 3:
    conversao = hex(numes)
    base = 'hexadecimal'
else:
    print('bicho burro é so as opções que ta ai em cima besta')

print('Aqui esta o resultado de sua conversão do numero {} parar a base {}. Resultado = {}'.format(numes, base, conversao [2:]))