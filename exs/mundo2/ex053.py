frase = str(input('digite uma frase para eu verificar se é um palindromo(digite sem acentos): '))
teste = frase.replace(' ', '')
teste1 = ''
for c in range (len(teste)-1, -1, -1):
    teste1 += teste[c]
    
if teste1 == teste:
    print('essa palavra é um palindromo')
else: 
    print('essa palavra não é um palindromo')