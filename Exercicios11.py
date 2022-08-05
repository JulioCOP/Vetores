#Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer
# um programa que calcule e escreva a maior e a menor altura do grupo, a média de
# altura das mulheres, e o número de homens.

maior=menor=0

n=int(input("Informe a quantidade de pessoas: "))

altura:[float]=[0 for x in range (n)]
genero: [str]=[0 for x in range (n)]

for i in range (n):
    altura[i]=float(input(f"Informe a altura da {i+1}º pessoa: "))
    genero[i]=str(input((f"Informe o genero da {i+1}º pessoa. [F] / [M] ? "))).strip().upper()[0]
for i in range(n):
    if i==0:
        maior=altura[i]
        menor=altura[i]
    else:
        if altura[i]>maior:
            maior=altura[i]
        elif altura[i]<menor:
            menor=altura[i]

contm=conth=alturam_total=media=0
for i in range(n):
    if genero[i]=='M':
        conth+=1
    else:
        contm += 1
        alturam_total += altura[i]
media = alturam_total / contm

print(f"A menor altura do grupo é {menor:.2f}")
print(f"A maior altura do grupo é {maior:.2f}")
print(f"A media de altura de mulheres é {media:.2f}")
print(f"Temos um total de {conth} homens.")