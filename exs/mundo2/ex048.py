soma = 0
for c in range(1, 501, 2):
    if c%3==0:
        soma += c
print('a soma dos numros impares divisiveis por 3 é igual a {}'.format(soma))