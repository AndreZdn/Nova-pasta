nome = str(input('qual seu nome: '))  
if nome == 'andre':
    print('que nome bonito')
elif nome == 'amanda':
    print('parabens voce tem o nome mais bonito de todos')
elif nome == 'Pedro' or nome == 'maria' or nome =='enzo':
    print('seu nome é muito comum no Brasil em ')
elif nome in 'Ana claudia jessica  juliana':
    print('belo nome feminino')
else: 
    print('seu nome é meio merda na verdade')
print('tenha um bom dia {}'.format(nome))
