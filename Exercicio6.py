#Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
#terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
#o vetor C gerado.

a=int(input("Informe o quantidades de valores para cada vetor: "))
vetorA:[int]=[0 for x in range(a)]
vetorB:[int]=[0 for x in range(a)]
vetorC:[int]=[0 for x in range(a)]
print("Informe valores para o VETOR A")
for i in range(a):
    vetorA[i]=int(input(" "))
print("Informe valores para o VETOR B")
for i in range(a):
    vetorB[i]=int(input(" "))
for i in range(a):
    vetorC[i]=vetorA[i]+vetorB[i]
print(f"O vetor C é: {vetorC}")