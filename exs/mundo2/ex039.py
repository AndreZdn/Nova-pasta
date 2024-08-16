from datetime import date 
Datu = date.today().year
dnac = int(input('digite seu ano de nascimento '))
genro = int(input('Voce se considera homem? sim[1]/não[2]'))
alisto = int(input('voce ja se alistou por acaso? sim[1]/não[2]'))

idade = Datu-dnac
if genro == 2:
    print('ai sim não precisa se alistar')
elif alisto == 1:
    print('ai sim ja resolveu esse BO')
elif idade<=17:
    print('é voce ainda não precisa se alistar para o exercito')
    falta = 18-idade
    print('e ainda falta {} anos para voce ir se alistar'.format(falta))
elif idade == 18:
    print('iae safado, ta na hora de se alista vagabundo?')
else:
    print('ja passou o tempo de voce se alistar pro exercito vagabundo ')
    atraso = idade - 18
    print('carai ja passou {} anos de atraso vai resolver esse BO ai chapa'.format(atraso))

