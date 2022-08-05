#Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles
# tiraram no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor.
# Depois, imprimir os nomes dos alunos aprovados, considerando aprovados aqueles cuja média
# das notas seja maior ou igual a 6.0 (seis).
media=0
qtd_alunos=int(input("Informe a quantidade de alunos: "))
nome: [str]=[0 for x in range(qtd_alunos)]
nota1:[float]=[0 for x in range(qtd_alunos)]
nota2:[float]=[0 for x in range(qtd_alunos)]


for i in range(qtd_alunos):
    print(f"Informe nome e as notas dos dois semestres do {i+1}º aluno")
    nome[i] = str(input())
    nota1[i] = float(input())
    nota2[i] = float(input())

for i in range(qtd_alunos):
    media = ((nota1[i] + nota2[i])) / 2
    if media>=6.0:
        print(f"OS ALUNOS APROVADOS SÃO: {nome[i]}")



