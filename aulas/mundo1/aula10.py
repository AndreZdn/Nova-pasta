nota1 = float(input('qual foi a primeira nota? '))
nota2 = float(input('qual foi a segunda nota? '))
m =(nota1 + nota2)/2
print('a sua média foi de {:.2}'.format(m))

# if m >= 6.0:
#     print('então você é o tal do genio então') 
# else:
#     print('carai burrão menor')

print ('então você é o tal do inteligente então'if m>=6 else 'carai menó burrão')