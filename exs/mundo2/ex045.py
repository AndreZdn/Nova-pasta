from random import randint
from time import sleep
print('Esse é um programa de JOKENPÔ e voce ira jogar contra o computador sera que voce consegue ganhar?')
pessoa= int(input('''Digite: 
[0]PEDRA; 
[1]PAPEL; 
[2]TESOURA:
Qual sera sua jogada?  '''))
computador = randint(0, 1)
itens = ['pedra', 'papel', 'tesoura']
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
# if pessoa == 0:
#     resposta = 'pedra'
# elif pessoa == 1:
#     resposta = 'papel'
# elif pessoa == 2:
#     resposta = 'tesoura'
# if computador == 0:
#     respostac = 'pedra'
# elif computador == 1:
#     respostac = 'papel'
# elif computador == 2:
#     respostac = 'tesoura'

if pessoa == computador:
    print('Deu empate, voce escolheu {} e o computador escolheu {}'.format(itens[pessoa], itens[computador]))
elif pessoa == 0 and computador ==2 or pessoa == 1 and computador == 0 or pessoa == 2 and computador == 1:
    print('parabens voce ganhou, voce escolheu {} e o computador escolheu {}'.format(itens[pessoa], itens[computador]))
elif computador == 0 and pessoa ==2 or computador == 1 and pessoa == 0 or computador == 2 and pessoa == 1:
    print('que pena voce perdeu, voce escolheu {} e o computador escolheu {}'.format(itens[pessoa], itens[computador]))
else :
    print('Boa genio tem 3 opção na tela e tu escrevre errado animal')