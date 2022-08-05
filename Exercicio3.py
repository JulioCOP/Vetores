#Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois,
# mostrar na tela a altura média das pessoas, e mostrar também a porcentagem de pessoas
# com menos de 16 anos,bem como os nomes dessas pessoas caso houver.
soma_alt=alt_med=0
perc_id=0
contid=0
p=int(input("Informe a quantidade de pessoas: "))
nome: [str]=[0 for x in range(p)]
idade: [int]=[0 for x in range(p)]
altura: [float]=[0 for x in range(p)]

for i in range (p):
    print(f"DADOS DA {i+1}ª PESSOA: ")
    nome[i]=str(input("Informe o nome deste usuario: "))
    idade[i]=int(input(f"Qual a idade de {nome[i]} ? "))
    altura[i]=float(input(f"Qual a altura de {nome[i]} ? "))

print()
print("DADOS GERAIS DOS USUARIOS")
soma_alt=alt_med=0
for i in range(p):
    soma_alt += altura[i]
alt_med = soma_alt / p
print(f"A altura média desses usuários é {alt_med:.2f}")
perc_id=0
contid=0
for i in range(p):
    if idade[i]<16:
        contid= contid + 1
perc_id= (contid/p)*100
print(f"O percentual de usuários menor que tem 16 anos é de {perc_id:.2f}%")
for i in range (p):
        if idade[i]<16:
            print(nome[i])
