a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

#Nesta etapa é verificado o menor número entre os 3 recebidos.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Nesta etapa é verificado o maior número entre os 3 recebidos.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("Dos números enviados, o número {} é o menor e {} é o maior.".format(menor, maior))