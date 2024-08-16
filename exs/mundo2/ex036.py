print('=-='*20)
print('sistema bancario de emprestimo')
print('=-='*20)
vcasa = float(input('Qual o valor da casa? '))
vsalario = float(input('Quanto o voce ganha por mes? '))
qanos = int(input('em quantos anos voce deseja pagar? '))
meses = qanos*12
valorPossivel = vsalario*0.3
if valorPossivel < vcasa/meses:
    print('parado ai caloteiro, eu sei que voce não vai conseguir pagar essa casa')
    
else:
    print('Tudo certo para realizarmos o financiamento para voce')
    print('A prestaçao vai ficar no valor de R${:.2f}' .format(vcasa/meses))