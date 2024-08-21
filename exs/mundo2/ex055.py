Pmaior = 0
Pmenor = 0
pessoaM = 0
pessoam = 0
for c in range(0,5):
    peso = int(input('digite o peso da {}°Pessoa '.format(c+1)))
    if c == 0:
        Pmaior = peso
        Pmenor = peso  
        #aqui eu to definindo o primeiro valor como o maior e como o menor para evitar a gambiarra
    if peso>=Pmaior:
        Pmaior = peso
        pessoaM = c

    if peso<= Pmenor:
        Pmenor = peso
        pessoam = c 
print('a pessoa que pesou mais foi a {}°pessoa pesando {}KG '.format(pessoaM+1, Pmaior))
print('e a pessoa que pesou menos foi a {}°pessoa pesando {}KG '.format(pessoam+1, Pmenor))