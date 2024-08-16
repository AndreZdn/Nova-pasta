from datetime import date
ano = date.today().year
maior = 0
menor = 0

for c in range(0,7):
    anon = int(input('digite o ano de nascimento da {}°Pessoa '.format(c+1)))
    if ano - anon >= 21:
        maior += 1
    else:
        menor += 1

print('Nesse conjunto de pessoas exitem {} pessoas que não passaram da maior idade e {} que ja passaram '.format(menor, maior))