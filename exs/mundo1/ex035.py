l1 = float(input('digite o valor do primeiro lado do triangulo '))
l2 = float(input('digite o valor do segundo lado do triangulo '))
l3 = float(input('digite o valor do terceiro lado do triangulo '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('é possivel formar um triangulo com essas medidas')
else:
    print('é impossivel formar um triangulo com essas medidas')