#Fazer um programa para ler um número inteiro N e depois um vetor de N números reais.
# Em seguida,mostrar na tela a média aritmética de todos elementos com três casas decimais.
# Depois mostrar todos os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.
media_a=soma=0
n=int(input("Informe a quantidade de valores para o vetor: "))
vetor:[float]=[0 for x in range(n)]
for x in range(n):
    vetor[x]=float(input("Digite um número: "))
    soma += vetor[x]
media_a=soma/n
print(f"A MÉDIA DOS VALORES É: {media_a:.2f}")
print("ELEMENTOS ABAIXO DA MÉDIA:")
for x in range (n):
    if vetor[x]<media_a:
        print(f"{vetor[x]:.1f}")