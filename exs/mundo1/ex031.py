KmViagem = float(input('digita quantos km voce vai viajar '))

if KmViagem <= 200:
    preço = KmViagem*0.5
    print('então tua passagem vai custar R${}'.format(preço))
else:
    preço = KmViagem*0.45
    print('então tua passagem vai custar R${}'.format(preço))