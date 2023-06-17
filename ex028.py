from random import  randint
# Importando todo o módulo random não foi possível utilizar o randint, decorrência talvez de algum bug ou erro.
print("-=-"*20)
computador = randint(0, 5) #Gera um valor aleatório para comparação com o valor do usuário
print("Vou pensar em um número entre 0 e 5. Tente adivinhar.")
print("-=-"*20)
print("Em que número eu pensei? ")


tentativa = int(input(print("Digite um número: "))) #Recebe um valor do usuário para comparar com o gerado.

if computador == tentativa: #Compara os valores e informa se forem iguais
    print("Parabéns, você acertou")
else: print("Que pena,o número correto era {},e você tentou {}!".format(computador, tentativa)) #Caso sejam diferentes, informa o usuário