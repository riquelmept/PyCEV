número = int(input("Digite o número inteiro que deseja converter: "))
print("\033[4;30mDigite para qual sistema de númeração deseja converter:\n\033[31m1 - Binário\n\33[35m2 - Octal\n\033[34m3 - Hexadecimal\n\033[m")
variável = int(input(""))

if variável == 1:
    bin_número = bin(número)
    print("\033[31mO número {} em binário é {}".format(número, bin_número))
elif variável == 2:
    oct_número = oct(número)
    print("\33[35mO número {} em octal é {}".format(número, oct_número))
elif variável == 3:
    hex_número = hex(número)
    print("\033[34mO número {} em hexadecimal é {}".format(número, hex_número))
else: print("Opção inválida, tente novamente!")