#Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades.
# Os nomes devem ser armazenados em um vetor, e as idades em um outro vetor. Depois,
# mostrar na tela o nome da pessoa mais velha.

np=int(input("Informe a quantidade de pessoas: "))
nome:[str]=[0 for x in range(np)]
idade:[int]=[0 for x in range (np)]
maisvelha= idade[0]

for y in range(np):
    print(f"Informe os dados da {y+1}º pessoa")
    nome[y]=str(input("Nome: "))
    idade[y]=int(input("Idade: "))
for y in range (np):
    if idade[y]>maisvelha:
        maisvelha=idade[y]
        cont=y

print(f"A pessoa mais velha é {nome[cont]}")