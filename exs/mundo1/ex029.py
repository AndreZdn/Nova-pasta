velocidade_carro = float(input('digita ai a velocidade que seu carro tava rei '))
velocidadeMaxima = float(input('agora ne informa ai qual era a velocidade maxima permitida? '))
if velocidade_carro >= velocidadeMaxima:
    multa = (velocidade_carro-velocidadeMaxima)* 7
    print ('ae seu merda passou do limite de velociade que era 80km/h tu vai ser multado no valor de R${}'.format(multa))
else:
    print('continue seguindo as leis de transito se não eu vou ir multar voce')