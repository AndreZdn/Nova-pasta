import random
from time import sleep

numerousuario = int(input('Seu desafio é tentar acertar o numero que o computador pensou de 1 a 5, lembrando que so sera consdirado numeros inteiros'))
sleep(3)
numerocomputador = random.randrange(1, 5)

if numerocomputador == numerousuario:
    print('parabens seu cagão acertou, o computador penssou em {} e voce digitou {}'.format(numerocomputador, numerousuario))
else: 
    print('foi mal mas tu erro feio, o computador pensou em {} e voce digitou {}'.format(numerocomputador, numerousuario))