#Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na
# tela a média aritmética somente dos números pares lidos, com uma casa decimal.
# Se nenhum número par for digitado, mostrar a mensagem "NENHUM NUMERO PAR"

n=int(input("Digite p número de valores do vetor: "))
a:[float]=[0 for x in range(n)]
for i in range(n):
    a[i]=float(input("Informe um valor: "))
m_aritimetica=soma=cont=0
print()
for i in range (n):
    if a[i]%2==0:
        cont+=1
        soma += a[i]
        m_aritimetica=soma/cont
if a[i]%2!=0:
    print("NENHUM NUMERO PAR")
else:
    print(f"Os números pares são: {a[i]}")
    print(f"E sua média é: {m_aritimetica:.2f} ")
