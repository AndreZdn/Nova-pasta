import random
nomes = [] 

nomes.append  (str(input('digite o nome do primeiro aluno ')))
nomes.append  (str(input('digite o nome do segundo aluno ')))
nomes.append  (str(input('digite o nome do terceiro aluno ')))
nomes.append  (str(input('digite o nome do quarto aluno ')))


nomesorteado = random.choices(nomes)
print('o aluno sorteado foi o {}'.format(nomesorteado))

