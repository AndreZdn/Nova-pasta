n1 = float(input('Qual foi sua primeira nota'))
n2 = float(input('Qual foi sua segunda nota'))
m = (n1+n2)/2
if m < 5:
    print('ta reprovado idiota media {}'.formta(m))
elif m<6.9:
    print('ta de recuperação, melhor estudar tua media foi {}'.format(m))
else:
    print('parabens ta aprovado, tua media foi {} '.format(m))