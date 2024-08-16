prnor = float(input('qual é o valor do produto?'))
condicao = int(input('''qual sera o metodo de pagamento? 
[1] A Vista no Dinheiro/Cheque.  
[2]à vista no Cartão 
[3] No cartão em até 2x 
[4] 3x ou mais no cartão'''))
if condicao == 1:
    pagar = prnor*0.9
    print('com esse metodo voce consegue {} de desconto e ira pagar somente {}'.format('10%', pagar))
elif condicao == 2:
    pagar = prnor*0.95
    print('com esse metodo voce consegue {} de desconto e ira pagar somente {}'.format('5%', pagar))
elif condicao == 3:
    print('com esse metodo voce pagara o valor normal de {}'.format(prnor))
elif condicao == 4:
    pagar = prnor*1.20
    print('com esse metodo voce tera que pagar um juros total de {}, e ira pagar o valor de {}'.format('20%', pagar))
else:
    print('voce digitou um numero invalido para o metodo de pagamento, tente novamente')