import random
v = 0
while True:
    player = int(input("Digite um número: "))
    computer = random.randint(0,10)
    totally = player + computer
    type = " "
    while type not in "PI":
        type = str(input("Par ou ímpar? [P/I]"))
    print(f'Você jogou {player} e o computador {computer}. Total de {totally} ', end=" ")
    print("DEU PAR" if totally % 2 == 0 else "DEU ÍMPAR")
    if type == "P":
        if totally % 2 == 0:
            print("Você VENCEU!!")
            v += 1
        else:
            print("Você PERDEU!!!")
            break
    elif type == "I":
        if totally % 2 == 1:
            print("Você VENCEU!!")
            v += 1
        else:
            print("Você PERDEU!!")
            break
    print("Vamos jogar novamente...")
print("END GAME")
