frase = input('digite qualquer frase ai meu chapa: ')
print('a letra "A" apareceu {} vezes na sua frase'.format(frase.upper().count('A')))
print(' é a primeira vez que a letra "A" apareceu foi na posição {} '.format(frase.strip().upper().find('A')+1))
print('e a ultima vez que a letra "A" apareceu foi na posição {}'.format(frase.strip().upper().rfind('A')+1))
  