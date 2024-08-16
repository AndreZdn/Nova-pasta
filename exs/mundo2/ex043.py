altura= float(input('qual a sua altura '))
massa = float(input('qual o seu peso '))
imc = massa/altura**2
if imc<18.5:
    print('voce esta abaixo do peso e seu imc é igual a {}'.format(imc))
elif imc<=25:
    print('voce esta no peso ideal e seu imc é igual a {}'.format(imc))
elif imc<=30:
    print('voce esta com sobrepeso e seu imc é igual a {}'.format(imc))
elif imc<=40:
    print('voce esta obeso e seu imc é igual a {}'.format(imc))
else:
    print('voce esta com obesidade morbida e seu imc é igual a {}'.format(imc))