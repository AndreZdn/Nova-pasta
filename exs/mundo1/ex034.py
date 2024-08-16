salario = float(input('digite seu salario '))
if salario <= 1250:
    salarioaumento = salario*1.15
else:
    salarioaumento = salario*1.10

print('seu novo salario sera de {}'.format(salarioaumento))