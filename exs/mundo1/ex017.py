import math

co = float(input('digite o cateto oposto de um trinagulo retangulo '))
ca= float(input('agora digite agora o cateto  adjacente '))

hip = math.hypot(co, ca)
print('a hipotenusa do triangulo de cateto oposto {} e de cateto adjacente {} é igual a {}'.format(co, ca, hip))