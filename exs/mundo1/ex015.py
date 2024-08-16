diaalu = int(input('quantos dias alugados? '))
kmr = float(input('quantos KM rodados? '))
valor = diaalu*60 + kmr*0.15
print('o valor a pagar é R$ {:.2f}'.format(valor))