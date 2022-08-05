#Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida,
#mostre na tela todos os números pares, e também a quantidade de números pares.

n=int(input("Informe quantos números serão digitados pelo usuário: "))
num:[int]=[0 for x in range (n)]
for i in range(n):
    num[i]=int(input("Digite um número inteiro: "))
print()
print("NUMEROS PARES:")
cont = 0
for i in range(n):
    if num[i]%2==0:
        print(num[i])
        cont += 1
print(f"A quantidade de números pares é {cont}")