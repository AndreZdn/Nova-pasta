l1 = float(input('primeiro lado '))
l2 = float(input('segundo lado'))
l3 = float(input('terceiro lado'))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    if l1 == l2 == l3:
        tipo = 'equilatero'
    elif l1!=l2!=l3!=l1:
        tipo = 'escaleno'
    else:
        tipo = 'isóceles'
    print('Com esses valores é possivel formar um triangulo do tipo {}'.format(tipo))
else:
    print('não é possivel formar um triangulo com esses valores')