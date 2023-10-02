núm = cont = soma = 0
núm = int(input("Digite um número [999 para parar]: "))
while True:
    núm = int(input("Digite um número [999 para parar]: "))    
    if núm == 999:
        break
    soma += núm
    cont += 1
print("Você digitou {} números e a soma entre eles foi {}.".format(cont, soma))