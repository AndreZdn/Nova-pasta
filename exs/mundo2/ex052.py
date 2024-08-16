
num = int(input('Verificador de numero primo, diga qual numero voce acha que é primo: '))
res = 'é primo'
for c in range(1, num):
    if num%c==0 and c!=1:
       res = 'não é primo'  
print('esse numero {}'.format(res))