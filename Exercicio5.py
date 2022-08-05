#Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida,
# mostrar na tela o maior número do vetor (supor não haver empates). Mostrar também
# a posição do maior elemento, considerando a primeira posição como 0 (zero).
maior=posmaior=0
n = int(input("Informe um valor real: "))
vetor:[float]=[0 for x in range(n)]
for i in range(n):
    vetor[i]=float(input("Digite um número: "))
for i in range(n):
    if i==1:
        maior=vetor[i]
    else:
        if vetor[i]>maior:
            maior=vetor[i]
            posmaior=i
print(f"O maior valor é {maior}")

print(f"A POSIÇÃO DO MAIOR NÚMERO É:{posmaior} ")




