soma= 0
for c in range(0, 6):
    num = int(input('escolha um numero para somar '))
    if num%2==0:
        soma += num
print('a soma dos numeros pares selecionados foram de {}'.format(soma))