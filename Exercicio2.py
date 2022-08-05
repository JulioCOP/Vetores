#Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
#- Imprimir todos os elementos do vetor
#- Mostrar na tela a soma e a média dos elementos do vetor
soma=media=0
n= int(input("Informe quantas vezes você quer repetir este processo: "))
vet:[float]=[0 for x in range (n)]
for i in range(0,n):
    vet[i]=float(input("Digite o(s) número(s): "))
    soma+=vet[i]
    media=soma/n
print()
print("OS VALORES DO VETOR SÃO: ")
for i in range (0,n):
    print(f"{vet[i]}", end=" ")
print(f"\nA soma dos valores do vetor é: {soma:.2f}")
print(f"\n A média dos valores do vetor é: {media:.2f}")