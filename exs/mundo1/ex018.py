import math


ang = float(input('digita ai um angulo rei '))
angrad = math.radians(ang)
cos = math.cos(angrad)
sen = math.sin(angrad)
tan = math.tan(angrad)
print('sobre o angulo de {:.2f}, seu cosseno é {:.2f}, seu seno é {:.2f} e sua tangente é {:.2f}'.format(ang, cos, sen, tan))